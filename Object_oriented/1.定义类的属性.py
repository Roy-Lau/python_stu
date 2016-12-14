#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Programer(object):
	hobby = 'Play Computer'

	def __init__(self, name, age, weight):
		self.name = name
		self._age = age
		self.__weight = weight

	def get_weight(self):
		return self.__weight

if __name__ = '__main__':
	programer = Programer('Albert', 25, 50)
	print dir(programer)
	print programer.__dict__
	print programer.get_weight()
	print programer.Programer__weight
	# 代码有问题，有时间修改
