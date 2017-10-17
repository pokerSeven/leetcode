# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 18:12'


class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.re = set()

		self.solve([],nums)
		r = []
		for x in self.re:
			r.append(list(x))
		return r


	def solve(self,cur_list, s_list):
		if not s_list:
			self.re.add(tuple(cur_list))
		else:
			for x in s_list:
				l1 = cur_list[:]
				l1.append(x)
				l2 = s_list[:]
				l2.remove(x)
				self.solve(l1,l2)

class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		self.nums = nums
		res = [nums[:]]

		while True:
			k = self.max_k()
			if k == -1:
				return res
			else:
				min_i = self.find_min(self.nums[k])
				self.nums[k] ,self.nums[min_i] = self.nums[min_i],self.nums[k]
				self.revers_list(self.nums,k + 1,len(self.nums) - 1)
				res.append(self.nums[:])

	def find_min(self, v):
		for i in range(len(self.nums))[::-1]:
			if self.nums[i] > v:
				return i

	def max_k(self):
		for i in range(len(self.nums))[::-1][:-1]:
			if self.nums[i - 1] < self.nums[i]:
				return i - 1
		return -1



	def revers_list(self,li,start,tail):
		while start < tail:
			li[start],li[tail] = li[tail],li[start]
			start += 1
			tail -= 1



s = Solution()
print s.permuteUnique([1,2,3])
