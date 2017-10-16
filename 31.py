# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/15 22:47'


class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype
		"""
		tail = len(nums) - 1
		cur = tail
		while cur >= 0:
			for i in range(len(nums)):
				if tail - i <= cur:
					break
				if nums[cur] < nums[tail - i]:
					nums[cur],nums[tail - i] = nums[tail - i],nums[cur]
					l1 = nums[:cur + 1]
					l2 = nums[cur + 1:]
					l2.sort()
					l1.extend(l2)
					for i in range(len(nums)):
						nums[i] = l1[i]
					return
			cur -= 1
		nums.sort()
		return nums

s = Solution()
nums = [1,3,2]
print s.nextPermutation(nums)

