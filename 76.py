# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/30 17:21'


class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		m_dict = {}
		begin = 0
		end = 0
		head = 0
		counter = len(t)
		import sys
		d = sys.maxint
		for c in t:
			if m_dict.has_key(c):
				m_dict[c] += 1
			else:
				m_dict[c] = 1

		for end, c in enumerate(s):
			if m_dict.has_key(c):
				if m_dict[c] > 0:
					counter -= 1
				m_dict[c] -= 1

			while counter == 0:
				if d > end - begin:
					d = end - begin
					head = begin
				if m_dict.has_key(s[begin]):
					if m_dict[s[begin]] == 0:
						counter += 1
						m_dict[s[begin]] += 1
					else:
						m_dict[s[begin]] += 1
				begin += 1

		if d < sys.maxint:
			return s[head:head + d + 1]
		else:
			return ""


s = Solution()
print s.minWindow(
	"bdab",
	"ab")

import copy
