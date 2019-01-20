#!/usr/bin/env python3

from .eth_client import EthClient
import docker, os

class Parity(EthClient):
	image = "parity/parity:stable"
	command = "--base-path=/ethereum --config=/ethereum/parity.toml"
	syncmode = "--light"

	def __init__(self, chain, syncmode):
		super().__init__(chain)
		self.chain_prefix = "--chain="
		if syncmode.lower() != "light":
			self.syncmode = ""
		client = docker.from_env()
		self.container = client.containers.run(self.get_image(), self.get_command(),
							detach=True, 
							name=self.get_hostname(), 
							ports=self.get_ports(),
							volumes=self.get_volumes(),
							network=self.get_network())

	def get_command(self):
		return self.chain_prefix + self.chain.lower() + " " + self.command + " " + self.syncmode