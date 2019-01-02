#!/usr/bin/env python3

from .eth_client import EthClient
import docker, os

class ChainlinkNode(EthClient):
	ports = {"6689/tcp":6689}
	volumes = {os.path.abspath("chainlink"):{"bind":"/chainlink","mode":"rw"}}
	hostname = "chainlink"
	image = "smartcontract/chainlink:latest"
	command = "n -p /chainlink/.password -a /chainlink/.api"

	def __init__(self, chain):
		super().__init__(chain)
		client = docker.from_env()
		self.container = client.containers.run(self.get_image(), self.get_command(),
							detach=True,
							hostname=self.get_hostname(),
							environment=self.get_env(),
							ports=self.get_ports(),
							volumes=self.get_volumes(),
							network=self.get_network())

	def get_command(self):
		return self.command

	def get_env(self):
		env = [line.rstrip('\n') for line in open('.env')]
		return env