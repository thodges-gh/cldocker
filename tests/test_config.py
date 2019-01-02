#!/usr/bin/env python3

import lib.config
import unittest, os

class TestConfig(unittest.TestCase):

	def setUp(self):
		self.config = lib.config.Config("n")
		with open(".env.example") as base_env:
			self.env = base_env.read()
		with open(".env", "w") as new_env:
			new_env.write(self.env)

	def test_config(self):
		self.assertEquals(self.config.defaults, "n")
		self.assertEquals(self.config.eth, True)
		self.assertEquals(self.config.url, "ETH_URL=ws://172.22.0.2:8546")
		self.assertEquals(self.config.chain_id, "ETH_CHAIN_ID=3")
		self.assertEquals(self.config.link, "LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280")
		self.assertEquals(self.config.chain, "Ropsten")
		self.assertEquals(self.config.client, "Parity")
		self.assertEquals(self.config.syncmode, "light")

	def test_set_eth(self):
		lib.config.input = lambda _: "y"
		self.config.set_eth()
		self.assertEquals(self.config.eth, False)

	def test_set_url(self):
		lib.config.input = lambda _: "ws://custom:8546"
		self.config.set_url()
		self.assertEquals(self.config.url, "ETH_URL=ws://custom:8546")

	def test_set_chain(self):
		lib.config.input = lambda _: "Rinkeby"
		self.config.set_chain()
		self.assertEquals(self.config.chain, "Rinkeby")
		self.assertEquals(self.config.chain_id, "ETH_CHAIN_ID=4")
		self.assertEquals(self.config.link, "LINK_CONTRACT_ADDRESS=0x01BE23585060835E02B77ef475b0Cc51aA1e0709")

	def test_set_client(self):
		lib.config.input = lambda _: "Geth"
		self.config.set_client()
		self.assertEquals(self.config.client, "Geth")

	def test_set_syncmode(self):
		lib.config.input = lambda _: "full"
		self.config.set_syncmode()
		self.assertEquals(self.config.syncmode, "full")

	def test_write_config(self):
		self.config.write_config()
		self.assertTrue(os.path.isfile(".env"))
		with open(".env") as env_file:
			content = [line.rstrip('\n') for line in env_file]
			self.assertEqual(content[10], "ETH_URL=ws://172.22.0.2:8546")
			self.assertEqual(content[11], "ETH_CHAIN_ID=3")
			self.assertEqual(content[12], "LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280")

	def tearDown(self):
		with open(".env.example") as base_env:
			self.env = base_env.read()
		with open(".env", "w") as new_env:
			new_env.write(self.env)