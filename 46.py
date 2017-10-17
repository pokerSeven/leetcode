# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 17:45'


class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.re = []

		self.solve([],nums)
		return self.re


	def solve(self,cur_list, s_list):
		if not s_list:
			self.re.append(cur_list)
		else:
			for x in s_list:
				l1 = cur_list[:]
				l1.append(x)
				l2 = s_list[:]
				l2.remove(x)
				self.solve(l1,l2)

s = Solution()
print s.permute([1,2,3])
