# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 15:49'


class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		for str in board:
			if not self.isCool(str):
				return False

		for i in range(9):
			str = ""
			for li in board:
				str.append(li[i])
			if not self.isCool(str):
				return False

		for i in range(9):
			str = ""
			for j in range(9):
				str.append(board[i/3*3 + j/3][i%3*3+j%3])
				if not self.isCool(str):
					return False

		return True

	def isCool(self, str):
		s_dict = {}
		for x in str:
			if x != ".":
				if s_dict.has_key(x):
					return False
				else:
					s_dict[x] = 1
		return True
