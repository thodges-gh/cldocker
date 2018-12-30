#!/bin/bash

set -e

# Looking for this:
# {"jsonrpc":"2.0","id":1,"result":false}

# But not when this:
# {"jsonrpc":"2.0","id":2,"result":"0x0"}

sync() {

  echo "Waiting 10 seconds then will begin watching sync status!"
  sleep 10

  # Initial check (before syncing has started)
  while true; do
    BLOCK=$`curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":2}' http://localhost:8545`
    if [[ $BLOCK != *"\"result\":\"0x0\""* ]]
    then
      break;
    fi
    echo "Waiting on syncing to start: $BLOCK"
    sleep 10
  done

  echo "Syncing has started!"

  # Now wait for syncing to complete
  while true; do
    STATUS=$`curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}' http://localhost:8545`
    if [[ $STATUS == *"\"result\":false"* ]]
    then
      break;
    fi
    echo "Waiting on syncing to complete: $STATUS"
    sleep 10
  done

  echo "Syncing is complete!"

  docker-compose -f chainlink.yml up
}