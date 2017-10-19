# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 15:32'


class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		n = int("".join(map(str, digits)))
		n = n + 1
		return map(int,list(str(n)))