# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/14 22:14'


class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		h_len = len(haystack)
		n_len = len(needle)
		if haystack == needle:
			return 0

		if not h_len:
			return -1

		for i in range(h_len):
			print  haystack[i:i + n_len]
			print needle
			if haystack[i:i + n_len] == needle:
				return i
		return -1

s = Solution()
print s.strStr("aa","a")