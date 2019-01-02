# Run Chainlink & Geth with Docker Compose

## Prerequisites

- [Docker](https://docs.docker.com/install/#supported-platforms)
- [Python](https://www.python.org/downloads/) (Version 3)
- [Git](https://git-scm.com/downloads)
- OpenSSL (should be installed on all Linux systems)
- (Optional but useful) Make

## General Setup and Run

Follow the link below for system-specific instructions
- [Amazon AWS](#amazon-aws-instructions)

Then run the following commands:

```bash
$ git clone https://github.com/thodges-gh/cldocker.git
$ cd cldocker
$ pip3 install -r requirements.txt
$ python main.py
```

If you have Make install, you can simply run the following after entering the directory:

```bash
$ make install
$ make setup
```

The setup script will display several prompts, each with a default value, and will start the node for you when complete. If you take the defaults for all the questions, it will spin up a Chainlink node and Parity light client on Ropsten when complete.

## Interacting with the Node

Navigate to http://localhost:6689/ to view the web interface. Use the same credentials that you entered in the setup script. If using a VPS, replace `localhost` with your instance's public IP.

Take note of your ETH address (get it from the Configuration page of the UI), you will need to send some ether to it in order to pay for gas. You can also get this from the node's Configuration page.

---

## Amazon AWS Instructions

Deploy Amazon Linux 2 AMI instance and connect

#### Install base programs:

```bash
$ sudo yum install -y git curl screen openssl make python3
```

#### Install Docker Compose and Setup Docker:

```bash
$ sudo amazon-linux-extras install docker
$ sudo systemctl start docker
$ sudo gpasswd -a $USER docker
$ exit
```

Log in again through `ssh`. Test that Docker works without sudo by running `docker ps`.

Follow the instructions under [General Setup and Run](#general-setup-and-run).