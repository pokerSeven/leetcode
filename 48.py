# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 18:51'


class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		new_matrix = matrix[::-1]
		res = []

		for i in range(len(matrix)):
			li = []
			for j in range(len(matrix[0])):
				li.append(new_matrix[j][i])
			res.append(li)
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				matrix[i][j] = res[i][j]

		return

class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		matrix[:] = zip(*matrix[::-1])
		return

s = Solution()
a = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(a)
print a

