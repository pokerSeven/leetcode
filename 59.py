# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 9:55'


class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		matrix = [[0 for x in range(n)] for x in range(n)]

		if n <= 0:
			return []

		direc = [[-1,0],[1,0],[0,-1],[0,1]]
		r_direc = [3,2,0,1]
		cur = 3
		positive = [0,0]
		for x in range(n*n):
			matrix[positive[0]][positive[1]] = x + 1
			if 0 <= positive[0] + direc[cur][0]< n and 0 <= positive[1] + direc[cur][1]< n and matrix[positive[0]+ direc[cur][0]][positive[1]+ direc[cur][1]] == 0:
				pass
			else:
				cur = r_direc[cur]
			positive[0] = positive[0] + direc[cur][0]
			positive[1] = positive[1] + direc[cur][1]
		return matrix

s = Solution()
print s.generateMatrix(4)
