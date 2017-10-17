# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 22:12'


class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if not matrix or not matrix[0]:
			return []

		direc = [[-1,0],[1,0],[0,-1],[0,1]]
		r_direc = [3,2,0,1]
		cur = 3
		positive = [0,0]
		res = []
		for x in range(len(matrix)*len(matrix[0])):
			res.append(matrix[positive[0]][positive[1]])
			matrix[positive[0]][positive[1]] = None
			if 0 <= positive[0] + direc[cur][0]< len(matrix) and 0 <= positive[1] + direc[cur][1]< len(matrix[0]) and matrix[positive[0]+ direc[cur][0]][positive[1]+ direc[cur][1]]:
				pass
			else:
				cur = r_direc[cur]
			positive[0] = positive[0] + direc[cur][0]
			positive[1] = positive[1] + direc[cur][1]
		return res



