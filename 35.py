# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 15:31'


class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		import sys

		if not nums:
			return [-1, -1]
		left = [0]
		right = [len(nums) - 1]
		while left[0] <= right[0]:
			if target < nums[left[0]] :
				return left[0]
			if  target > nums[right[0]]:
				return right[0] + 1
			medium = (left[0] + right[0]) / 2
			if nums[medium] > target:
				right[0] = medium
			elif nums[medium] < target:
				left[0] = medium + 1
			else:
				return medium

s = Solution()
print s.searchInsert([1,3,5,6],0)
