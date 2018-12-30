#!/bin/bash

ROPSTEN_NETWORK="ETH_CHAIN_ID=3
LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280"
RINKEBY_NETWORK="ETH_CHAIN_ID=4
LINK_CONTRACT_ADDRESS=0x01BE23585060835E02B77ef475b0Cc51aA1e0709"
KOVAN_NETWORK="ETH_CHAIN_ID=42
LINK_CONTRACT_ADDRESS=0xa36085F69e2889c224210F603D836748e7dC0088"

run_command() {
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
      echo "Permissions required to run $1 command" >&2
      exit 0
    fi
    return $status
}

# Enable custom ETH_URL
while true; do
  read -p "Custom ETH_URL (Y or N) [N]? " custom
  [ -z "$custom" ] && custom=N
  case $custom in
   [yY]* ) read -p "Enter the URL: " url
           echo $'\r\n'"ETH_URL=$url" >> .env
           break;;

   [nN]* ) echo $'\r\n'"ETH_URL=ws://eth:8546" >> .env
           break;;

   * )     echo "Enter Y or N, please."; 
  esac
done

# Select network
while true; do
    read -p "Available networks:
  Ropsten: 3
  Rinkeby: 4
  Kovan: 42 
  Your choice? [3]: " network 
  [ -z "$network" ] && network=3
    case $network in
    3 )  echo $'\r\n'"$ROPSTEN_NETWORK" >> .env
          break;;

    4 )  echo $'\r\n'"$RINKEBY_NETWORK" >> .env
          break;;

    42 ) echo $'\r\n'"$KOVAN_NETWORK" >> .env
          break;;

    * )  echo "Please select a valid network."; 
    esac
  done

# Select client
if [[ $custom == [nN]* ]]
then
  # Sync mode
  while true; do
    read -p "Light client? [Y]: " light
    [ -z "$light" ] && light=Y
    case $light in
    [yY]* ) break;;

    [nN]* ) sed "s/light/fast/g" ./ethereum/geth.toml > ./ethereum/geth.toml.new
            mv ./ethereum/geth.toml.new ./ethereum/geth.toml
            sed "s/light = true/light = false/g" ./ethereum/parity.toml > ./ethereum/parity.toml.new
            mv ./ethereum/parity.toml.new ./ethereum/parity.toml
            break;;

    * )     echo "Enter Y or N, please."; 
    esac
  done
  # Populate for Rinkeby
  if [ $network -eq 4 ]
  then
    sed "s/NetworkId = 3/NetworkId = 4/g" ./ethereum/geth.toml > ./ethereum/geth.toml.new
    mv ./ethereum/geth.toml.new ./ethereum/geth.toml
    sed "s/--testnet/--rinkeby/g" ./geth.yml > ./geth.yml.new
    mv ./geth.yml.new ./geth.yml
    DOCKER_COMPOSE_RUN_COMMAND="docker-compose -d -f geth.yml up"

  # Populate for Kovan
  elif [ $network -eq 42 ]
  then
    sed "s/ropsten/kovan/g" ./ethereum/parity.toml > ./ethereum/parity.toml.new
    mv ./ethereum/parity.toml.new ./ethereum/parity.toml
    DOCKER_COMPOSE_RUN_COMMAND="docker-compose -d -f parity.yml up"

  # Set up Ropsten
  else
    # Geth or Parity
    while true; do
    read -p "Geth or Parity? [P]arity: " gepa
    [ -z "$gepa" ] && gepa=P
    case $gepa in
    [gG]* ) DOCKER_COMPOSE_RUN_COMMAND="docker-compose -d -f geth.yml up"
            break;;

    [pP]* ) DOCKER_COMPOSE_RUN_COMMAND="docker-compose -d -f parity.yml up"
            break;;

    * )     echo "Enter G or P, please."; 
    esac
  done
  fi
else
  DOCKER_COMPOSE_RUN_COMMAND="docker-compose -f chainlink.yml up"
fi

run_command docker swarm init

wallet_password=$(systemd-ask-password "Enter the wallet password:")

echo "$wallet_password" > ".password"

api_user=$(systemd-ask-password "Enter the API email:")
api_password=$(systemd-ask-password "Enter the API password:")

echo "$api_user"$'\r\n'"$api_password" > ".api"

run_command docker secret create wallet_password .password
run_command docker secret create api_password .api

run_command openssl req -x509 -out server.crt  -keyout server.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

run_command mv server.* chainlink/tls/

echo "Setup complete!"

run_command $DOCKER_COMPOSE_RUN_COMMAND

if [[ $custom == [nN]* ]]
then
  ./syncing.sh
fi