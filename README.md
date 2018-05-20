# Run Chainlink & Geth with Docker Compose

## Prerequisites

- Install [Docker Compose](https://docs.docker.com/compose/install/#install-compose)
- Install [Docker](https://docs.docker.com/install/#supported-platforms)
- Install git

## Setup and Run

```bash
$ git clone https://github.com/thodges-gh/cldocker.git
$ cd cldocker
$ mkdir chainlink/keys
$ cp /path/to/keystore chainlink/keys/
$ export KEYSTORE_PASS="my super secure password"
$ docker-compose up
```

Re-run `docker-compose up` after Geth's sync is complete to free up memory.

## Interacting with the Node

```bash
$ docker exec cldocker_chainlink_1 chainlink h
```