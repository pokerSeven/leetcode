# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 15:35'


class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		return bin(int(a,base=2) + int(b,base=2)).replace("0b","")