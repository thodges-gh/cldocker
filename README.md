# Run Chainlink & Ethereum containers with Docker

## Prerequisites

- [Docker](https://docs.docker.com/install/#supported-platforms)
- [Python](https://www.python.org/downloads/) (Version 3)
- [Git](https://git-scm.com/downloads)
- Make
- OpenSSL (should be installed on all Linux systems)

## General Setup and Run

Follow the link below for system-specific instructions
- [Amazon AWS](#amazon-aws-instructions)

Clone this repo and enter the directory:

```bash
git clone https://github.com/thodges-gh/cldocker.git && cd cldocker
```

Now run the following commands after entering the directory:

```bash
make install
make setup
```

The setup script will display several prompts, each with a default value, and will start the node for you when complete. If you take the defaults for all the questions, it will spin up a Parity light client on Ropsten and prompt you for information about the node (passwords and API user).

## Interacting with the Node

Navigate to https://localhost:6689/ to view the web interface. Use the same credentials that you entered in the setup script. If using a VPS, replace `localhost` with your instance's public IP. By default the node uses a self-signed certificate, so your browser may complain about that, simply add an exception (Firefox) or continue anyway (Chrome) to access the GUI.

The first thing you should do once signed in is take note of your ETH address by going to the Configuration page of the UI, you will need to send some ether to it in order for the node to pay for gas.

You can follow the logs of all containers by running:

```bash
make logs
```

Or to just view the output of the Chainlink container(s):

```bash
make logs-cl
```

Or just the Ethereum container:

```bash
make logs-eth
```

## Starting and stopping

After you have gone through the setup, you can use the following commands to maintain the containers.

### Chainlink node

To start a new Chainlink container instance:

```bash
make start-cl
```

To stop running Chainlink containers:

```bash
make stop-cl
```

To perform a rolling upgrade:
- Pulls latest image
- Starts a new container with the port incremented
- Stops the old container

```bash
make update-cl
```

To pull the latest Chainlink image:

```bash
make pull-cl
```

### Ethereum client

To restart the Ethereum client:

```bash
make restart-eth
```

To stop the Ethereum client:

```bash
make stop-eth
```

To pull the latest (stable) image for your Ethereum client:

```bash
make pull-geth
```

Or

```bash
make pull-parity
```

## Resetting the environment file

Run the following command:

```bash
make clean
```

This will reset the environment file to its defaults. You will then need to run `make setup` again before starting nodes.

---

## Amazon AWS Instructions

Deploy Amazon Linux 2 AMI instance and connect

#### Install base programs:

```bash
sudo yum install -y git curl screen openssl make python3
```

#### Install Docker Compose and Setup Docker:

```bash
sudo amazon-linux-extras install docker
sudo systemctl start docker
sudo gpasswd -a $USER docker
exit
```

Log in again through `ssh`. Test that Docker works without sudo by running `docker ps`.

Follow the instructions under [General Setup and Run](#general-setup-and-run).
