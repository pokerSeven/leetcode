# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 8:30'


class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		for i,x in enumerate(nums):
			 while 0 < nums[i] <= len(nums) and nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
				x = nums[i]
				nums[x-1] ,nums[i] = nums[i], nums[x-1]

		print nums
		for i, x in enumerate(nums):
			if x  != i + 1:
				return i + 1
		return len(nums) + 1

s  = Solution()
print s.firstMissingPositive([1,1])
