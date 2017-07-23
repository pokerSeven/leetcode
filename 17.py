# -*- coding: utf-8 -*-
"""
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		int_string = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
		if digits == "":
			return []
		elif len(digits) == 1:
			return [x for x in int_string.get(digits)]

		return [x + y for x in int_string.get(digits[0]) for y in self.letterCombinations(digits[1:])]


s = Solution()
print s.letterCombinations("234")
