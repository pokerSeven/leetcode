# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 19:19'


class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		flag = [True]
		if n < 0:
			flag[0] = False
			n = - n
		if n == 0:
			return 1
		bin_n = bin(n).replace('0b', '')
		bin_n = list(bin_n)[::-1]

		d = [x for i in range(len(bin_n))]
		for i in range(1, len(d)):
			d[i] = d[i - 1] * d[i - 1]

		re = [1.0]
		print d[1] * re[0]

		for i,v in enumerate(bin_n):
			if v == "1":
				re[0] = re[0] * d[i]
		if flag:
			return re[0]
		else:
			return 1/re[0]

s = Solution()
print s.myPow(3,3)





