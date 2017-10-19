# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 15:20'


class Solution(object):
	def minPathSum(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		if not obstacleGrid :
			return 0

		for i in range(1, len(obstacleGrid[0])):
			obstacleGrid[0][i] = obstacleGrid[0][i - 1] + obstacleGrid[0][i]
		for i in range(1, len(obstacleGrid)):
			obstacleGrid[i][0] = obstacleGrid[i - 1][0] + obstacleGrid[i][0]
		for x in range(1, len(obstacleGrid)):
			for y in range(1, len(obstacleGrid[0])):
				obstacleGrid[x][y] = min(obstacleGrid[x - 1][y] , obstacleGrid[x][y - 1]) + obstacleGrid[x][y]
		return obstacleGrid[-1][-1]

s = Solution()
print s.minPathSum([[0]])
