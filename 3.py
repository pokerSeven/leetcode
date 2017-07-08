# -*- coding: utf-8 -*-
"""
Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        stop  = 0
        start_n = 0
        stop_n = 0
        dict = {}
        for i,x in enumerate(s):
            if dict.get(x) is not None:
                stop_n = i - 1
                if stop - start < stop_n -start_n:
                    stop = stop_n
                    start = start_n
                start_n = dict[x] + 1
            dict[x] = i
            print start,stop
        if stop == 0 and start == 0:
            return 1
        return stop - start + 1


