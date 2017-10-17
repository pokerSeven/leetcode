# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 19:09'


class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		di = {}

		for str in strs:
			s1 = list(str)
			s1.sort()
			s = "".join(s1)
			if di.has_key(s):
				di[s].append(str)
			else:
				di[s] = [str]
		re = []
		for _,d in di.items():
			re.append(d)
		return re


