#!/usr/bin/env python3

from .docker_client import DockerClient
import docker, os

class ChainlinkNode(DockerClient):
	volumes = {os.path.abspath("chainlink"):{"bind":"/chainlink","mode":"rw"}}
	image = "smartcontract/chainlink:latest"
	command = "n -p /chainlink/.password -a /chainlink/.api"

	def __init__(self, host_port):
		super().__init__()
		self.ports = {"6689/tcp":host_port}
		client = docker.from_env()
		self.container = client.containers.run(self.get_image(), self.get_command(),
							detach=True,
							environment=self.get_env(),
							ports=self.ports,
							volumes=self.get_volumes(),
							network=self.get_network())

	def get_command(self):
		return self.command

	def get_env(self):
		env = [line.rstrip('\n') for line in open('.env')]
		return env