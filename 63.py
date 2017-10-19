# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 12:37'


class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
			return 0

		obstacleGrid[0][0] = 1
		for i in range(1, len(obstacleGrid[0])):
			if obstacleGrid[0][i] == 1:
				obstacleGrid[0][i] = 0
			else:
				obstacleGrid[0][i] = obstacleGrid[0][i - 1]
		for i in range(1, len(obstacleGrid)):
			if obstacleGrid[i][0] == 1:
				obstacleGrid[i][0] = 0
			else:
				obstacleGrid[i][0] = obstacleGrid[i - 1][0]
		for x in range(1, len(obstacleGrid)):
			for y in range(1, len(obstacleGrid[0])):
				if obstacleGrid[x][y] == 1:
					obstacleGrid[x][y] = 0
				else:
					obstacleGrid[x][y] = obstacleGrid[x - 1][y] + obstacleGrid[x][y - 1]
		return obstacleGrid[-1][-1]


s = Solution()
print s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]])
