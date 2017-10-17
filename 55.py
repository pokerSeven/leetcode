# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 23:21'


class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		max_right = 0

		for i , v in enumerate(nums):
			if i > max_right:
				return False
			if max_right >= len(nums) - 1:
				return True
			max_right = max(max_right,i + v)

s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])
