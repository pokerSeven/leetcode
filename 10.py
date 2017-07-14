# -*- coding: utf-8 -*-
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        if len(p) >= 2 and p[1] == "*":
            if self.isMatch(s,p[2:]):
                return True
            if len(s) > 0 and (s[0] == p[0] or p[0] == "."):
                if self.isMatch(s[1:],p):
                    return True
        elif len(s) > 0 and len(p) > 0 and(s[0] == p[0] or p[0] == "."):
            if self.isMatch(s[1:],p[1:]):
                return True
        return False

r = Solution()
print r.isMatch("aab",".*")


