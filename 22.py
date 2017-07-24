# -*- coding: utf-8 -*-
"""
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		return self.gP(2 * n, 0)

	def gP(self, n, s):
		if s == n:
			result = ""
			for i in range(s):
				result += ")"
			return [result]
		else:
			ans = []
			if s > 0:
				return ["(" + x for x in self.gP(n - 1, s + 1)] + [")" + x for x in self.gP(n - 1, s - 1)]
			else:
				return ["(" + x for x in self.gP(n - 1, s + 1)]


class Solution1(object):
	def generateParenthesis(self, n):
		def generate(p, left, right, parens=[]):
			print parens
			if left:
				generate(p + '(', left - 1, right)
			if right > left:
				generate(p + ')', left, right - 1)
			if not right:
				print parens,p
				parens += p,
			return parens

		return generate('', n, n)


s = Solution1()
print s.generateParenthesis(2)
