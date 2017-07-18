# -*- coding: utf-8 -*-
"""
12. Integer to Roman
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        c = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
             ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
             ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
             ["", "M", "MM", "MMM"]]
        roman = ""
        roman += c[3][(num / 1000) % 10]
        roman += c[2][(num / 100) % 10]
        roman += c[1][(num / 10) % 10]
        roman += c[0][num  % 10]
        return roman

s  = Solution()
print s.intToRoman(1984)


