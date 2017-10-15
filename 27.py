# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/14 21:26'


# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements of nums being 2.

class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		n = len(nums)
		m = [0, -1]
		for i, x in enumerate(nums):
			if x == val:
				m[0] += 1
				if m[1] == -1:
					m[1] = i
			elif x != val and m[1] != -1:
				print nums
				print m[1]
				nums[m[1]], nums[i] = nums[i], nums[m[1]]
				m[1] += 1
		return n - m[0]

	def removeElement2(self,nums,val):
		n = len(nums)
		m = [0]
		for i, x in enumerate(nums):
			if x != val:
				nums[m[0]] = nums[i]
				m[0] += 1
		return m[0]



