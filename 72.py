# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/19 9:50'


class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		ans = 0

		temp = []
		word2 = list(word2)
		for w1 in word1:
			k = -1
			try:
				k = word2.index(w1,0, len(word2))
			except:
				pass
			if k != -1:
				temp.append(k)
				word2[k] = "$"
		ans += abs(len(word2) - len(word1))
		ans += min(abs(len(temp) - len(word1)),abs(len(temp) - len(word2)))
		dp = [1 for x in range(len(temp))]
		for i in range(len(temp)):
			for j in range(i+1,len(temp)):
				if temp[i] < temp[j]:
					dp[j] = max(dp[j],dp[i]+1)
		m = 0
		for v in dp:
			m = max(v,m)
		return ans + len(temp) - m


class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""

		dp = [[0 for x in range(len(word1) + 1)] for x in range(len(word2)+1)]
		for i in range(len(dp)):
			dp[i][0] = i
		for i in range(len(dp[0])):
			dp[0][i] = i

		for i in range(len(dp) - 1):
			for j in range(len(dp[0]) -1):
				if word1[j] == word2[i]:
					dp[i+1][j+1] = dp[i][j]
				else:
					dp[i + 1][j + 1] = min(dp[i][j]+1,dp[i+1][j]+1,dp[i][j+1]+1)
		return dp[-1][-1]







s = Solution()
print s.minDistance("a","d")
