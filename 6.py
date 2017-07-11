# -*- coding: utf-8 -*-
"""
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "":
            return ""

        st = ["" for x  in range(numRows)]

        direction = 1
        index = 0
        for x in s:
            if index < numRows and index >= 0:
                st[index] = st[index] + x
                index  = index + direction
            else:
                direction = direction * -1
                index = index + 2 * direction
                st[index] = st[index] + x
                index = index + direction

        for x in st:
            print ":",x
        return  reduce(lambda x1, x2 : x1 + x2,st)

s = Solution()
print s.convert("PAYPALISHIRING",1)