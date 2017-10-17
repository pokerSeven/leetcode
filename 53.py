# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 21:52'


class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		re = [nums[0]]
		temp = [0]
		for x in nums:
			temp[0] += x
			re[0] = max(temp[0], re[0])
			if temp[0] < 0:
				temp[0] = 0
		return re[0]

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

