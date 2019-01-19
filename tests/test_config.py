#!/usr/bin/env python3

import lib.config
import unittest, os
from mock import MagicMock

class TestConfig(unittest.TestCase):

	def setUp(self):
		self.config = lib.config.Config("n")
		with open(".env.example") as base_env:
			self.env = base_env.read()
		with open(".env", "w") as new_env:
			new_env.write(self.env)

	def test_config(self):
		self.assertEqual(self.config.defaults, "n")
		self.assertEqual(self.config.eth, True)
		self.assertEqual(self.config.url, "ETH_URL=ws://172.22.0.2:8546")
		self.assertEqual(self.config.chain_id, "ETH_CHAIN_ID=3")
		self.assertEqual(self.config.link, "LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280")
		self.assertEqual(self.config.chain, "Ropsten")
		self.assertEqual(self.config.client, "Parity")
		self.assertEqual(self.config.syncmode, "light")

	def test_set_eth_y(self):
		inputs = ["y", "Y", "yes", "YES"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_eth()
			self.assertEqual(self.config.eth, False)

	def test_set_eth_n(self):
		inputs = ["n", "N", "no", "NO"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_eth()
			self.assertEqual(self.config.eth, True)

	def test_set_url(self):
		lib.config.input = lambda _: "ws://custom:8546"
		self.config.set_url()
		self.assertEqual(self.config.url, "ETH_URL=ws://custom:8546")

	def test_set_chain_ropsten(self):
		inputs = ["Ropsten", "ropsten", "3", "testnet"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_chain()
			self.assertEqual(self.config.chain, "ropsten")
			self.assertEqual(self.config.chain_id, "ETH_CHAIN_ID=3")
			self.assertEqual(self.config.link, "LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280")

	def test_set_chain_rinkeby(self):
		inputs = ["Rinkeby", "rinkeby", "4"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_chain()
			self.assertEqual(self.config.chain, "rinkeby")
			self.assertEqual(self.config.chain_id, "ETH_CHAIN_ID=4")
			self.assertEqual(self.config.link, "LINK_CONTRACT_ADDRESS=0x01BE23585060835E02B77ef475b0Cc51aA1e0709")

	def test_set_chain_kovan(self):
		inputs = ["Kovan", "kovan", "42"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_chain()
			self.assertEqual(self.config.chain, "kovan")
			self.assertEqual(self.config.chain_id, "ETH_CHAIN_ID=42")
			self.assertEqual(self.config.link, "LINK_CONTRACT_ADDRESS=0xa36085F69e2889c224210F603D836748e7dC0088")

	def test_set_client_geth(self):
		inputs = ["Geth", "geth", "GETH"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_client()
			self.assertEqual(self.config.client, "geth")

	def test_set_client_parity(self):
		inputs = ["Parity", "parity", "PARITY"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_client()
			self.assertEqual(self.config.client, "parity")

	def test_set_syncmode_light(self):
		inputs = ["y", "Y", "yes", "YES"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_syncmode()
			self.assertEqual(self.config.syncmode, "light")

	def test_set_syncmode_full(self):
		inputs = ["n", "N", "no", "NO"]
		for val in inputs:
			lib.config.input = lambda _: val
			self.config.set_syncmode()
			self.assertEqual(self.config.syncmode, "full")

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