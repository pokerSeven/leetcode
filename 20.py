# -*- coding: utf-8 -*-
"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"(" : 0, "{": 0,"[":0}
        for x in s:
            if d.get(x) is not None:
                d[x] += 1

            else:
                if x is ")":
                    if d.get("(") <= 0:
                        return False
                    else:
                        d["("] -= 1
                if x is "}":
                    if d.get("{") <= 0:
                        return False
                    else:
                        d["{"] -= 1
                if x is "]":
                    if d.get("[") <= 0:
                        return False
                    else:
                        d["["] -= 1
        for _,i in d.items():
            if i != 0:
                return False
        return True
s = Solution()
print s.isValid("{}{}()()({")
print s.isValid("{}{}()()")