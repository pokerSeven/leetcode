# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 13:29'


class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		for i, x in enumerate(nums):
			if x == target:
				return i
		return -1
