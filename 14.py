# -*- coding: utf-8 -*-
"""
 Longest Common Prefix

 Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = 0
        i = 0
        if strs == []:
            return 0
        while True:
            c = ""
            for x in strs:
                if c == "" and len(x) > i:
                    c = x[i]
                if len(x) > i and x[i] == c:
                    pass
                else:
                    return i
            i += 1
s = Solution()
print s.longestCommonPrefix(["1","12"])