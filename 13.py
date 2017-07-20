# -*- coding: utf-8 -*-
"""
13. Roman to Integer
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
             "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
             "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900,
             "M": 1000, "MM": 2000, "MMM": 3000}

        if s == "":
            return 0
        s += "$"
        result = 0
        while True:
            if s == "$":
                break
            for i in range(1, len(s) + 1):
                if d.get(s[:i]) is  None:
                    result += d.get(s[:i - 1])
                    s = s[i-1:]
                    break
        return result

s = Solution()
print s.romanToInt("XIII")
