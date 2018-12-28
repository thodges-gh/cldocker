#!/bin/bash

run_command() {
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
      echo "Permissions required to run $1 command" >&2
      exit 0
    fi
    return $status
}

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