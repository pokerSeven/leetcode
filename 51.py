# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 20:48'


class Solution(object):
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		cur = [0]
		que_list = [-1 for x in range(n)]
		res = []

		while True:
			if cur[0] == -1:
				return res
			if cur[0] == n:
				res.append(self.ans(que_list))
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

	def ans(self,que_list):
		a_list = []
		for i in range(len(que_list)):
			a = [""]
			for j in range(len(que_list)):
				if j == que_list[i]:
					a[0] = a[0] + "Q"
				else:
					a[0] = a[0] + "."
			a_list.append(a[0])
		return a_list

s = Solution()
print s.solveNQueens(4)
