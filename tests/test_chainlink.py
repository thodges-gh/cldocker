#!/usr/bin/env python3

import lib.chainlink
import lib.config
import unittest

class TestChainlinkNode(unittest.TestCase):

	def setUp(self):
		self.node = lib.chainlink.ChainlinkNode("Ropsten")
		self.config = lib.config.Config("y")
		self.config.write_config()

	def test_chainlink(self):
		self.assertEqual(str(self.node.container.image), "<Image: 'smartcontract/chainlink:latest'>")
		self.assertEqual(self.node.container.status, "created")

	def test_get_command(self):
		self.assertEqual(self.node.get_command(), "n -p /chainlink/.password -a /chainlink/.api")

	def test_get_env(self):
		env = self.node.get_env()
		self.assertEqual(env[10], "ETH_URL=ws://172.22.0.2:8546")
		self.assertEqual(env[11], "ETH_CHAIN_ID=3")
		self.assertEqual(env[12], "LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280")

	def tearDown(self):
		self.node.container.stop()
		with open(".env.example") as base_env:
			self.env = base_env.read()
		with open(".env", "w") as new_env:
			new_env.write(self.env)