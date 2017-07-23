# -*- coding: utf-8 -*-
"""
 3Sum Closest
 Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1 .

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums = sorted(nums)
		i = 0
		result = None
		closet = None
		while i < len(nums):
			if i == 0 or nums[i] != nums[i - 1]:
				left = i + 1
				right = len(nums) - 1
				while left < right:
					if closet == None:
						closet = abs(target - (nums[i] + nums[left] + nums[right]))
						result = nums[i] + nums[left] + nums[right]
					if target - (nums[i] + nums[left] + nums[right]) < 0:
						if closet > abs(target - (nums[i] + nums[left] + nums[right])):
							closet = abs(target - (nums[i] + nums[left] + nums[right]))
							result = nums[i] + nums[left] + nums[right]
						right -= 1
					elif target - (nums[i] + nums[left] + nums[right]) > 0:
						if closet > abs(target - (nums[i] + nums[left] + nums[right])):
							closet = abs(target - (nums[i] + nums[left] + nums[right]))
							result = nums[i] + nums[left] + nums[right]
						left += 1
					else:
						return nums[i] + nums[left] + nums[right]
			i = i + 1
		return result


class Solution1(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums = sorted(nums)
		i = 0
		result = nums[0] + nums[1] + nums[2]
		closet = abs(target - (nums[0] + nums[1] + nums[2]))
		while i < len(nums):
			if i == 0 or nums[i] != nums[i - 1]:
				left = i + 1
				right = len(nums) - 1
				while left < right:
					s = nums[i] + nums[left] + nums[right]
					if abs(target - result) > abs(target - s):
						ans = s
						if s == target:
							return s
					if s > target:
						right -= 1
					else:
						left += 1
			i = i + 1
		return result

s = Solution()
print s.threeSumClosest([0,2,1,-3], 1)
