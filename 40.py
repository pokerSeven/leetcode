# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 22:30'

class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		candidates.sort()
		self.candidates = candidates
		self.res = []
		self.solve(0,target,[])
		return self.res


	def solve(self,index, target,values):
		for i in range(index ,len(self.candidates)):
			if self.candidates[i] == target:
				v = values[:]
				v.append(target)
				self.res.append(v)
				return True
			elif self.candidates[i] < target:
				v = values[:]
				v.append(self.candidates[i])
				self.solve(i+1,target - self.candidates[i],v)
		return
