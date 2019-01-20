#!/usr/bin/env python3

from .docker_client import DockerClient
import docker, os

class EthClient(DockerClient):
	ports = {"8546/tcp":8546,"8545/tcp":8545,"30303/udp":30303,"30303/tcp":30303}
	volumes = {os.path.abspath("ethereum"):{"bind":"/ethereum","mode":"rw"}}
	hostname = "eth"

	def __init__(self, chain):
		self.chain = chain
		client = docker.from_env()
		try:
			client.networks.get("chainlink")
		except:
			client.networks.create("chainlink", driver="bridge")