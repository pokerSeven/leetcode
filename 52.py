# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 21:42'


class Solution(object):
	def totalNQueens(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		cur = [0]
		que_list = [-1 for x in range(n)]
		res = [0]

		while True:
			if cur[0] == -1:
				return res[0]
			if cur[0] == n:
				res[0] += 1
				cur[0] -= 1
				continue

			que_list[cur[0]] += 1
			if que_list[cur[0]] >= n:
				que_list[cur[0]] = -1
				cur[0] -= 1
				continue

			if self.isIn(que_list,cur[0],que_list[cur[0]]):
				cur[0] += 1
				continue

	def isIn(self,q_list,x,y):
		for i in range(x):
			x1 = i
			y1 = q_list[i]
			if abs(x1 - x) == abs(y1 - y) or x1 - x == 0 or y1 - y == 0:
				return False
		return True


s = Solution()
print s.totalNQueens(4)
