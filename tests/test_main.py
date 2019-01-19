#!/usr/bin/env python3

import main
import unittest, os

class TestMain(unittest.TestCase):

    files = ["chainlink/.api", "chainlink/.password", "chainlink/tls/server.crt", "chainlink/tls/server.key"]

    def setUp(self):
        for filename in self.files:
            try:
                os.remove(filename)
            except OSError:
                pass

    def test_clean(self):
        with open(".env", "a") as env_file:
            env_file.write("TEST DATA" + "\n")
        main.clean()
        self.assertTrue(os.path.isfile(".env"))
        with open(".env") as env_file:
            content = [line.rstrip('\n') for line in env_file]
            self.assertEqual(len(content), 10)

    def test_generate_certs(self):
        cert_files = ["chainlink/tls/server.crt", "chainlink/tls/server.key"]
        main.generate_certs()
        for filename in cert_files:
            self.assertTrue(os.path.isfile(filename))

    def test_create_wallet_password(self):
        main.input = lambda _: "password"
        main.create_wallet_password()
        self.assertTrue(os.path.isfile("chainlink/.password"))
        with open("chainlink/.password") as password_file:
            content = [line.rstrip('\n') for line in password_file]
            self.assertEqual(content[0], "password")

    def test_create_api_email(self):
        main.input = lambda _: "user@example.com"
        main.create_api_email()
        self.assertTrue(os.path.isfile("chainlink/.api"))
        with open("chainlink/.api") as api_file:
            content = [line.rstrip('\n') for line in api_file]
            self.assertEqual(content[0], "user@example.com")

    def test_create_api_password(self):
        self.test_create_api_email()
        main.input = lambda _: "api_password"
        main.create_api_password()
        self.assertTrue(os.path.isfile("chainlink/.api"))
        with open("chainlink/.api") as api_file:
            content = [line.rstrip('\n') for line in api_file]
            self.assertEqual(content[1], "api_password")

    def tearDown(self):
        for filename in self.files:
            try:
                os.remove(filename)
            except OSError:
                pass