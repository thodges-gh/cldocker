# Run Chainlink & Geth with Docker Compose

## Prerequisites

- [Docker](https://docs.docker.com/install/#supported-platforms)
- [Docker Compose](https://docs.docker.com/compose/install/#install-compose)
- git
- OpenSSL

## General Setup and Run

Follow the link below for system-specific instructions
- [Amazon AWS](#amazon-aws-instructions)

Then run the following commands:

```bash
$ git clone https://github.com/thodges-gh/cldocker.git
$ cd cldocker
$ ./setup.sh
```

If you chose to use a custom `ETH_URL`, run the following command:

```bash
$ docker-compose -f chainlink.yml up
```

Otherwise, run:

```bash
$ docker-compose up
```

The included `.env` file is set up for use on the Ropsten test network. If you wish to change networks, you will need to modify the `ETH_CHAIN_ID` and `LINK_CONTRACT_ADDRESS` values, as well as the argument for the command to run Geth in the `docker-compose.yml` file. It may take a few minutes for the Ethereum client to begin syncing. 

Take note of your ETH address, you will need to send some ether to it in order to pay for gas. You can also get this from the node's Configuration page.

## Interacting with the Node

Navigate to http://localhost:6689/ to view the web interface. Use the same credentials that you entered in the setup script. If using a VPS, replace `localhost` with your instance's public IP.

#### Running commands

Use this command as an example for the available Chainlink commands:

```bash
$ docker-compose exec chainlink chainlink h
```

Attach to the Geth console:

```bash
$ docker-compose exec geth geth attach /ethereum/geth.ipc
```

## Updating Container Images

```bash
$ docker-compose stop
$ docker-compose pull
$ docker-compose up --build
```

---

## Amazon AWS Instructions

Deploy Amazon Linux 2 AMI instance and connect

#### Install base programs:

```bash
$ sudo yum install -y git curl screen openssl
```

#### Install Docker Compose and Setup Docker:

```bash
$ sudo amazon-linux-extras install docker
$ sudo systemctl start docker
$ sudo gpasswd -a $USER docker
$ exit
```

Log in again through `ssh`. Test that Docker works without sudo by running `docker ps`.

Then follow the instructions [here](https://docs.docker.com/compose/install/#install-compose) to install and setup docker-compose.

Follow the instructions under [General Setup and Run](#general-setup-and-run).