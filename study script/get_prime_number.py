# -*- coding:utf-8 -*-  
# !/usr/bin/python
#_author__='wancaihong'
#__date__='2019/4/7 12:05'

"""
case:获取100以内的质数
"""

import unittest

class logintest(unittest.TestCase):

	def test_get_prime_number(self):
		list = []
		for i in range(2, 100):
			for j in range(2, i):
				if i%j == 0:
					break
			else:
				list.append(i)
		print(list)