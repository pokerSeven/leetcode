# -*- coding: utf-8 -*-
"""
String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0

        flag = 1
        index = 0
        while str[index] == ' ':
            index = index + 1
        if str[index] == '-':
            flag = -1
            index = index + 1
        elif str[index] == '+':
            index = index + 1
        if index >= len(str) or str[index] < '0' or str[index] > '9':
            return 0
        last = index
        while last < len(str) and (str[last] >= '0'and str[last] <= '9'):
            last = last + 1
        reint =   int(str[index:last]) * flag
        if reint > 2147483647:
            return 2147483647
        if reint < -2147483648:
            return -2147483648
        return reint