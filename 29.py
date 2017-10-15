# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/15 10:27'


# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		if divisor == 0:
			import sys
			return sys.maxint
		if dividend == 0:
			return 0
		positive = True
		if dividend < 0:
			dividend = - dividend
			positive = not positive
		if divisor < 0:
			divisor = - divisor
			positive = not positive
		r = [0]
		while dividend -divisor >= 0:
			temp , i = divisor, 1
			while dividend - temp >= 0:
				dividend -= temp
				r[0] += i
				i <<= 1
				temp <<= 1
		if not positive:
			r[0] = -r[0]
		return min(max(-2147483648, r[0]), 2147483647)


