# -*- coding: utf-8 -*-
"""
Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1

        reInt = int(str(x*flag)[::-1])*flag

        if reInt < -2147483648 or reInt > 2147483647:
            return 0
        else:
            return reInt