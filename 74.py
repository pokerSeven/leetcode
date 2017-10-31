# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/30 16:50'


class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		for li in matrix:
			if li:
				if  li[0]<= target <= li[-1]:
					try:
						li.index(target)
						return True
					except:
						return False
		return False
