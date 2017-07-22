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
        d_push = {"(": ")", "[": "]", "{": "}"}
        d_pop = {")": "(", "]": "[", "}": "{"}
        d_stack = []
        for x in s:
            if d_push.has_key(x):
                d_stack.append(x)
            else:
                if len(d_stack) > 0 and d_stack[-1] == d_pop.get(x):
                    d_stack.pop()
                else:
                    return False
        if d_stack:
            return False
        else:
            return True


s = Solution()
print s.isValid("(")
print s.isValid("]")
