# -*- coding: utf-8 -*-

import yaml


class Config():
	def __init__(self, file_name):
		self.data = None
		self.read_config(file_name)

	def read_config(self, file_name):
		with open(file_name, encoding='utf8') as file:
			self.data = yaml.load(file, Loader=yaml.FullLoader)

	def __getitem__(self, item):
		return self.data[item]
