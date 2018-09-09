# Run Chainlink & Geth with Docker Compose

## Prerequisites

- [Docker Compose](https://docs.docker.com/compose/install/#install-compose)
- [Docker](https://docs.docker.com/install/#supported-platforms)
- git

## General Setup and Run

```bash
$ git clone https://github.com/thodges-gh/cldocker.git
$ cd cldocker
/* create or edit your .env, .api, and .password files now */
$ docker swarm init
$ docker secret create wallet_password .password
$ docker secret create api_password .api
$ docker-compose up
```

It may take a few minutes to begin syncing (meanwhile the Chainlink node is constantly restarting) and you may need to `tail` the Chainlink node's log file or attach to the container to view the output. 

Take note of your ETH address, you will need to send some ether to it in order to pay for gas.

## Interacting with the Node

Navigate to http://localhost:6688/ to view the web interface. Use the same credentials that you stored in the `.api` file to sign in.

#### Running commands

Use this command as an example for the available Chainlink commands:

```bash
$ docker-compose exec chainlink chainlink h
```

Attach to the Geth console:

```bash
$ docker-compose exec geth geth attach /ethereum/geth.ipc
```

#### Watching logs

```bash
$ tail -f chainlink/log.jsonl
```

## Updating Container Images

```bash
$ docker-compose stop
$ docker-compose pull
$ docker-compose up --build
```

---

## Amazon AWS Instructions

Deploy Amazon Linux AMI instance and connect

#### Install base programs:

```bash
$ sudo yum install -y git curl screen docker
```

#### Install Docker Compose and Setup Docker:

```bash
$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo /etc/init.d/docker start
$ sudo chkconfig docker on
$ sudo gpasswd -a $USER docker
$ logout
```

Log in again through ssh. Test that Docker works without sudo by running `docker ps`.

#### Clone and enter the repo:

```bash
$ git clone https://github.com/thodges-gh/cldocker.git
$ cd cldocker
$ docker swarm init
$ docker secret create wallet_password .password
$ screen
$ docker-compose up
```
