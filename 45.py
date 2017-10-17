# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 15:58'


class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		s = set()
		n = len(nums)
		re = [1]
		if n == 1:
			return 0

		s.add(0)
		while True:
			temp_set = set()
			for x in s:
				if nums[x] + x >= n - 1:
					return re[0]
				else:
					for i in range(nums[x]):
						temp_set.add(x + i+ 1)
			s = temp_set
			re[0] += 1
		return re[0]

class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		temp = [-1 for i in range(n)]

		temp[0] = 0

		for i in range(n):
			if i + nums[i] + 1>= n:
				if temp[n - 1] == -1:
					return temp[i] + 1
				else:
					return temp[n-1]
			for j in range(nums[i]):
				if temp[i + j + 1] == -1:
					temp[i + j + 1] = temp[i] + 1
		return temp[-1]

class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if n <= 1:
			return 0
		self.nums = nums
		t = [n - 1]
		re = [0]
		while True:
			if t[0] == 0:
				return re[0]
			else:
				t[0] = self.solve(t[0])
				re[0] += 1

	def solve(self,tail):
		for i,x in enumerate(self.nums):
			if i + x >= tail:
				return i


class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		re = [0]
		temp = [0,0]

		while True:
			if n - 1 <= temp[1]:
				return re[0]
			max_n = [temp[1]]
			for i in range(temp[0],temp[1]+ 1):
				max_n[0]  = max(i + nums[i],max_n[0])
			temp[0],temp[1] = temp[1],max_n[0]
			re[0]+=1






s = Solution()
