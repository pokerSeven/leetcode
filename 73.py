# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/30 16:39'


class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		import copy
		re_matrix = copy.deepcopy(matrix)
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if re_matrix[i][j] == 0:
					for x in range(len(matrix)):
						matrix[x][j] = 0
					for y in range(len(matrix[0])):
						matrix[i][y] = 0

s = Solution()
a = [[0,1]]
s.setZeroes(a)
print a