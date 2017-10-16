# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 16:36'


class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""

		self.board = board
		self.row = [dict() for i in range(9)]
		self.col = [dict() for i in range(9)]
		self.rc = [dict() for i in range(9)]

		for i, li in enumerate(board):
			for j, x in enumerate(li):
				if x != ".":
					self.row[i][x] = (i, j)
					self.col[j][x] = (i, j)
					self.rc[i / 3 * 3 + j / 3][x] = (i, j)
		self.solve()
		return self.board


	def del_dict(self,i,j):
		x = self.board[i][j]
		self.row[i].pop(x)
		self.col[j].pop(x)
		self.rc[i / 3 * 3 + j / 3].pop(x)

	def insert_dict(self,i,j):
		x = self.board[i][j]
		self.row[i][x] = (i, j)
		self.col[j][x] = (i, j)
		self.rc[i / 3 * 3 + j / 3][x] = (i, j)

	def solve(self):
		if self.isEnd():
			return True
		for i, li in enumerate(self.board):
			for j, x in enumerate(li):
				if x == ".":
					for k in range(9):
						k = str(k+1)
						if self.isCool(i,j,k):
							self.board[i][j] = k
							self.insert_dict(i,j)
							if self.solve():
								return True
							self.del_dict(i,j)
							self.board[i][j] = "."
					return False

	def isEnd(self):
		for di in self.row:
			if len(di) != 9:
				return False
		for di in self.col:
			if len(di) != 9:
				return False
		for di in self.rc:
			if len(di) != 9:
				return False
		return True


	def isCool(self, i, j,k):
		if self.row[i].has_key(k):
			return False
		if self.col[j].has_key(k):
			return False
		if self.rc[i / 3 * 3 + j / 3].has_key(k):
			return False
		return True




s = Solution()
xx = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print s.solveSudoku(xx)
print(xx)