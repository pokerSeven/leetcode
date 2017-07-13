# -*- coding: utf-8 -*-
"""
 Palindrome Number
 Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = x
        x2 = 0
        while x1 > 0:
            x2 *= 10
            x2 += x1 % 10
            x1 /= 10
        if x2 == x:
            return True
        return False