#!/usr/bin/env python3

import main, lib.config, tests.test_main
import unittest, os
from docker import APIClient

class TestIntegrations(unittest.TestCase):

	files = ["chainlink/.api", "chainlink/.password", "chainlink/tls/server.crt", "chainlink/tls/server.key"]

	def setUp(self):
		self.config = lib.config.Config("n")
		with open(".env.example") as base_env:
			self.env = base_env.read()
		with open(".env", "w") as new_env:
			new_env.write(self.env)

	def test_fresh_start_ethereum(self):
		container = main.fresh_start_ethereum(self.config)
		self.assertIsNotNone(container)

	def test_restart_ethereum_running(self):
		container = main.fresh_start_ethereum(self.config)
		self.assertIsNotNone(container)
		result = main.restart_ethereum()
		self.assertTrue(result)

	def test_restart_ethereum_not_running(self):
		result = main.restart_ethereum()
		self.assertFalse(result)

	def test_start_chainlink(self):
		container = main.start_chainlink(6689)
		self.assertIsNotNone(container)

	def test_update_chainlink_existing(self):
		self.config.write_config()
		main.generate_certs()
		main.input = lambda _: "user@example.com"
		main.create_api_email()
		main.input = lambda _: "password"
		main.create_api_password()
		main.create_wallet_password()
		container = main.start_chainlink(6689)
		self.assertEqual(container.ports["6689/tcp"], 6689)
		self.assertIsNotNone(container)
		new_container = main.update_chainlink()
		self.assertEqual(new_container.ports["6689/tcp"], 6690)

	def tearDown(self):
		for filename in self.files:
			try:
				os.remove(filename)
			except OSError:
				pass
		with open(".env.example") as base_env:
			self.env = base_env.read()
		with open(".env", "w") as new_env:
			new_env.write(self.env)
		cli = APIClient()
		for container in cli.containers(filters={"status":"running"}):
			cli.stop(container)
			cli.remove_container(container)