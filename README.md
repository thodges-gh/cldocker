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
git clone https://github.com/thodges-gh/cldocker.git
cd cldocker
```

Now run the following commands after entering the directory:

```bash
make install
make setup
```

The setup script will display several prompts, each with a default value, and will start the node for you when complete. If you take the defaults for all the questions, it will spin up a Parity light client on Ropsten and prompt you for information about the node (passwords and API user).

## Interacting with the Node

Navigate to http://localhost:6689/ to view the web interface. Use the same credentials that you entered in the setup script. If using a VPS, replace `localhost` with your instance's public IP.

Take note of your ETH address (get it from the Configuration page of the UI), you will need to send some ether to it in order to pay for gas. You can also get this from the node's Configuration page.

You can follow the logs of each container by first running `docker ps`, then `docker logs -f container_name`.

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
