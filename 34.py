# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 15:03'


class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if not nums:
			return [-1,-1]
		left = [0]
		right = [len(nums) - 1]
		while left[0] <= right[0]:
			if target < nums[left[0]] or target > nums[right[0]]:
				return [-1,-1]
			medium = (left[0] + right[0])/2
			if nums[medium] > target:
				right[0] = medium
			elif nums[medium] < target:
				left[0] = medium +  1
			else:
				re = [medium,medium]
				while re[0] > 0:
					if nums[re[0] - 1] == target:
						re[0] -= 1
					else:
						break
				while re[1] < len(nums) - 1:
					if nums[re[1] + 1] == target:
						re[1] += 1
					else:
						break
				return re
		return [-1,-1]


s = Solution()
print s.searchRange([1,4],1)

