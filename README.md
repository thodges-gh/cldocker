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

The setup script will display several prompts, each with a default value, and will start the node for you when complete. If you take the defaults for all the questions, it will spin up a Chainlink node and Parity light client on Ropsten when complete.

Take note of your ETH address, you will need to send some ether to it in order to pay for gas. You can also get this from the node's Configuration page.

## Troubleshooting

### Issues while syncing

When using the "light" sync mode on Geth or Parity, it is fairly common for the Ethereum client to lose peers. When this happens, it will effect the syncing script to start the Chainlink node, most likely (and by-design) by stopping it all-together. The Ethereum client should continue syncing, and you can verify this by running `docker ps` to see its current status and one of the following (depending on your Ethereum client) commands to follow the logs.

Geth:

```bash
$ docker-compose -f geth.yml logs -f
```

Parity:

```bash
$ docker-compose -f parity.yml logs -f
```

If you start the Chainlink node before syncing of the blockchain has completed, then the Chainlink node will have to receive and store the headers for every block on the network. This is unnecessary since no run requests for that Chainlink node would have existed before it was initialized. It is suggested to wait until the sync is complete before starting the Chainlink node.

### Issues after syncing

Also when using a light client, it may occasionally lose peers even after syncing has completed. If this happens, the Chainlink node will continuously restart until a good connection is re-established. There shouldn't be any need to do anything further.

## Interacting with the Node

Navigate to http://localhost:6689/ to view the web interface. Use the same credentials that you entered in the setup script. If using a VPS, replace `localhost` with your instance's public IP.

#### Running commands

Use this command as an example for the available Chainlink commands:

```bash
$ docker-compose -f chainlink.yml exec chainlink chainlink h
```

Attach to the Geth console:

```bash
$ docker-compose -f geth.yml exec geth geth attach /ethereum/geth.ipc
```

## Updating Container Images

```bash
$ docker-compose -f chainlink.yml pull
$ docker-compose -f chainlink.yml down
$ docker-compose -f chainlink.yml up
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

Then follow the instructions [here](https://docs.docker.com/compose/install/#install-compose) to install and setup docker-compose. Select the "Linux" tab under the Install Compose header.

Follow the instructions under [General Setup and Run](#general-setup-and-run).