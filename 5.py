# -*- coding: utf-8 -*-
"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        d = {}
        start_n = 0
        stop_n = 0
        for i, x in enumerate(s):
            if d.get(x) is None:
                d[x] = []
            d[x].append(i)

        for i, x in enumerate(s):
            if len(s) - i > stop_n - start_n:
                for st in d[x][::-1]:
                    if st - i > stop_n - start_n and self.isPalindrome(s, i,st):
                        start_n = i
                        stop_n = st
                        break
            else:
                return s[start_n:stop_n + 1]
        return s[start_n:stop_n + 1]

    def isPalindrome(self, s, start, stop):

        while start < stop:
            if s[start] != s[stop]:
                return False
            start = start + 1
            stop = stop - 1
        return True

class Solution1(object):
    def longestPalindrome(self,s):
        if s == "":
            return ""
        new_s = "$" + "#" + "#".join(s) + "#"

        max_right = 0
        pos = 0
        RL = [0 for i in new_s]
        max_pos = 0
        for i in range(len(new_s)):
            if i <= max_right:
                RL[i] = min(RL[2*pos -i],max_right - i)
            k = RL[i]
            while i - k >= 0 and i + k < len(new_s) and new_s[i - k] == new_s[i+k]:
                k += 1
            RL[i] = k
            if RL[i] + i > max_right:
                max_right = RL[i] + i
                pos= i

            if RL[i] > RL[max_pos]:
                max_pos = i
        return new_s[max_pos -RL[max_pos] + 1:max_pos + RL[max_pos] - 1].replace("#","")




s = Solution1()
print s.longestPalindrome("abbbv")
#print s.isPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",0,999)