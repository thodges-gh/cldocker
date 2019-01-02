#!/usr/bin/env python3

import docker, os

class EthClient:
	ports = {"8546/tcp":8546,"8545/tcp":8545,"30303/udp":30303,"30303/tcp":30303}
	volumes = {os.path.abspath("ethereum"):{"bind":"/ethereum","mode":"rw"}}
	network = "chainlink"

	def __init__(self, chain):
		self.chain = chain
		client = docker.from_env()
		try:
			client.networks.get("chainlink")
		except:
			client.networks.create("chainlink", driver="bridge")

	@classmethod
	def get_image(cls):
		return cls.image

	@classmethod
	def get_ports(cls):
		return cls.ports

	@classmethod
	def get_volumes(cls):
		return cls.volumes

	@classmethod
	def get_hostname(cls):
		return cls.hostname

	def get_network(self):
		return self.network

	def get_ip(self):
		ip = None
		client = docker.from_env()
		try:
			ip = client.networks.get("chainlink").attrs['Containers'][self.container.attrs['Id']]['IPv4Address']
			ip = ip[:-3]
		except:
			ip = "172.22.0.2"
		return ip