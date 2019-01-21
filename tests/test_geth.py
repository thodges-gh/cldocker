#!/usr/bin/env python3

from docker import APIClient
import lib.geth
import unittest

class TestGeth(unittest.TestCase):

	def setUp(self):
		cli = APIClient()
		try:
			cli.remove_container("eth")
		except:
			pass
		self.client = lib.geth.Geth("Ropsten", "light")

	def test_geth(self):
		self.assertEqual(str(self.client.container.image), "<Image: 'ethereum/client-go:stable'>")
		self.assertEqual(self.client.container.status, "created")

	def test_get_command(self):
		self.assertEqual(self.client.get_command(), "--testnet --datadir=/ethereum --config=/ethereum/geth.toml --syncmode=light")

	def tearDown(self):
		self.client.container.stop()
		self.client.container.remove()