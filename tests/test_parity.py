#!/usr/bin/env python3

from docker import APIClient
import lib.parity
import unittest

class TestParity(unittest.TestCase):

	def setUp(self):
		cli = APIClient()
		try:
			cli.remove_container("eth")
		except:
			pass
		self.client = lib.parity.Parity("Ropsten", "light")

	def test_parity(self):
		self.assertEqual(str(self.client.container.image), "<Image: 'parity/parity:stable'>")
		self.assertEqual(self.client.container.status, "created")

	def test_get_command(self):
		self.assertEqual(self.client.get_command(), "--chain=ropsten --base-path=/ethereum --config=/ethereum/parity.toml --light")

	def tearDown(self):
		self.client.container.stop()
		self.client.container.remove()