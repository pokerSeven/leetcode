# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 10:53'

import time




class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		temp_list = []
		max_n = [0]
		for x in s:
			if x == "(":
				temp_list.append(1)
			else:
				temp_list.append(-1)
		for i in range(len(temp_list)):
			if temp_list[i] == -1:
				m = [0]
				m[0] = i
				while m[0] > 0:
					m[0] -= 1
					if temp_list[m[0]] == 1:
						temp_list[m[0]] = 0
						temp_list[i] = 0
						break
					elif temp_list[m[0]] == -1:
						break
		k = [0]
		for x in temp_list:
			if x == 0:
				k[0] += 1
			else:
				max_n[0] = max(max_n[0],k[0])
				k[0] = 0
		max_n[0] = max(max_n[0], k[0])
		return max_n[0]

class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		stk = [-1]

		max_n = [0]
		for i in range(len(s)):
			t = stk[-1]
			if t != -1 and s[t] == "(" and s[i] == ")":
				stk.pop()
				max_n[0] = max(max_n[0],i-stk[-1])
			else:
				stk.append(i)
		return max_n[0]

s = Solution()
print time.localtime()
print s.longestValidParentheses("()()")