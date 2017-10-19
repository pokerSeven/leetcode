# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 9:43'


class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		w = 0
		re = 0
		for x in s:
			if x == " ":
				if w != 0:
					re, w = w, 0
			else:
				w += 1
		if w != 0:
			return w
		else:
			return re