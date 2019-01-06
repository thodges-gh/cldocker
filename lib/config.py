#!/usr/bin/env python3

class Config:

	valid_yesorno_answers = ["y", "n", "yes", "no"]
	valid_chain_answers = ["3", "4", "42", "ropsten", "rinkeby", "kovan", "testnet"]
	valid_client_answers = ["geth", "parity"]

	def __init__(self, defaults):
		self.defaults = defaults
		self.eth = True
		self.url = "ETH_URL=ws://172.22.0.2:8546"
		self.chain_id = "ETH_CHAIN_ID=3"
		self.link = "LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280"
		self.chain = "Ropsten"
		self.client = "Parity"
		self.syncmode = "light"

	def set_custom_fields(self):
		self.set_eth()
		if self.eth == False:
			self.set_url()
		self.set_chain()
		if self.eth:
			self.set_client()
			self.set_syncmode()

	def set_eth(self):
		custom_url = self.prompt("Do you want to use a custom ETH_URL? [N]: ", "n", self.valid_yesorno_answers)
		if custom_url[:1].lower() == "y":
			self.eth = False

	def set_url(self):
		self.url = "ETH_URL=" + input('Enter the URL: ')

	def set_eth_ip(self, ip):
		self.url = "ETH_URL=ws://" + ip + ":8546"

	def set_chain(self):
		chain_answer = self.prompt("What chain would you like? [Ropsten]: ", "ropsten", self.valid_chain_answers)
		if chain_answer.lower() == "ropsten" or chain_answer.lower() == "3" or chain_answer.lower() == "testnet":
			self.chain = "ropsten"
			self.chain_id = "ETH_CHAIN_ID=3"
			self.link = "LINK_CONTRACT_ADDRESS=0x20fe562d797a42dcb3399062ae9546cd06f63280"
		elif chain_answer.lower() == "rinkeby" or chain_answer.lower() == "4":
			self.chain = "rinkeby"
			self.chain_id = "ETH_CHAIN_ID=4"
			self.link = "LINK_CONTRACT_ADDRESS=0x01BE23585060835E02B77ef475b0Cc51aA1e0709"
		elif chain_answer.lower() == "kovan" or chain_answer.lower() == "42":
			self.chain = "kovan"
			self.chain_id = "ETH_CHAIN_ID=42"
			self.link = "LINK_CONTRACT_ADDRESS=0xa36085F69e2889c224210F603D836748e7dC0088"

	def set_client(self):
		if self.chain.lower() == "rinkeby":
			self.client = "geth"
		elif self.chain.lower() == "kovan":
			self.client = "parity"
		else:
			self.client = self.prompt("What client would you like, Geth or Parity? [Parity]: ", "parity", self.valid_client_answers)

	def set_syncmode(self):
		yn_syncmode = self.prompt("Light client? [Y]: ", "y", self.valid_yesorno_answers)
		if yn_syncmode[:1].lower() == "y":
			self.syncmode = "light"
		else:
			self.syncmode = "full"

	def write_config(self):
		with open(".env", "a") as env_file:
			env_file.write(self.url + "\n")
			env_file.write(self.chain_id + "\n")
			env_file.write(self.link + "\n")

	def prompt(self, question, default, answer_list):
		answer = input(question) or default
		if answer.lower() in answer_list:
			return answer.lower()
		else:
			self.prompt(question, default, answer_list)