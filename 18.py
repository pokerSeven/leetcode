# -*- coding: utf-8 -*-
"""
4Sum
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

"""


class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums = sorted(nums)
		a = 0
		result = []
		while a < len(nums):
			if a == 0 or nums[a] != nums[a-1]:
				b = a + 1
				while b < len(nums):
					if b == a + 1 or nums[b] != nums[b-1]:
						c = b + 1
						d = len(nums) - 1
						while c < d:
							if nums[a] + nums[b] + nums[c] + nums[d] < target:
								c += 1
							elif nums[a] + nums[b] + nums[c] + nums[d] > target:
								d -= 1
							else:
								result.append((nums[a],nums[b],nums[c],nums[d]))
								while c < d and nums[c] == nums[c+1]:
									c += 1
								while c < d and nums[d] == nums[d-1]:
									d -= 1
								c += 1
								d -= 1
					b += 1
			a += 1
		return result
s = Solution()
print s.fourSum([-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
,0)

