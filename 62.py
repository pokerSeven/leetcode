# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 12:12'


class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		c1 = 0
		c2 = 0
		c3 = 0

		temp = 1
		for i in range(1,m+n-1):
			temp *= i
			if i == m - 1:
				c1 = temp
			if i == n - 1:
				c2 = temp
			if i == m+n-1-1:
				c3 = temp


		return c3/c2/c1
