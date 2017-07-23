# -*- coding: utf-8 -*-
"""
15. 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums_len = len(nums)
		if nums < 3:
			return []
		nums = sorted(nums)
		result = set()
		for i in range(nums_len):
			for j in range(i + 1, nums_len):
				for k in range(j + 1, nums_len):
					if nums[i] + nums[j] + nums[k] == 0:
						result.add((nums[i], nums[j], nums[k]))
		return list(result)


class Solution1(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		d = {}
		for x in nums:
			if d.get(x) is None:
				d[x] = 1
			else:
				d[x] += 1

		result = set()
		for x, _ in d.iteritems():
			if d.get(x) == 1:
				d.pop(x)
			else:
				d[x] -= 1
			for y, _ in d.iteritems():
				if d.get(y) == 1:
					d.pop(y)
				else:
					d[y] -= 1
				if d.get(-x - y) is not None:
					result.add(tuple(sorted([x, y, -x - y])))
				if d.get(y) is None:
					d[y] = 1
				else:
					d[y] += 1
			if d.get(x) is None:
				d[x] = 1
			else:
				d[x] += 1
		return list(result)


class Solution2(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums = sorted(nums)
		i = 0
		result = []
		while i < len(nums):
			if i == 0 or nums[i] != nums[i - 1]:
				left = i + 1
				right = len(nums) - 1
				while left < right:
					if - nums[i] < nums[left] + nums[right]:
						right -= 1
					elif -nums[i] > nums[left] + nums[left]:
						left += 1
					else:
						result.append((nums[i], nums[left], nums[right]))
						while left < right and nums[left] == nums[left + 1]:
							left += 1
						while left < right and nums[right] == nums[right + 1]:
							right -= 1
						left += 1
						right -= 1
			i = i + 1
		return result


s = Solution2()
print s.threeSum(
	[-1, 0, 1, 2, -1, -4])
