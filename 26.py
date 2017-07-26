# -*- coding: utf-8 -*-
"""
26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		i = 0
		n = 0
		while i < len(nums):
			if i != 0 and nums[i] == nums[i - 1]:
				i += 1
				continue
			nums[n] = nums[i]
			n += 1
			i += 1
		return n
