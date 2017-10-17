# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 23:32'


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		def my_cmp(x,y):
			if x.start < y.start:
				return -1
			elif x.start > y.start:
				return 1
			else:
				if x.end < y.end:
					return -1
				elif x.end > y.end:
					return 1
				else:
					return 0

		intervals.sort(cmp=my_cmp)
		if not intervals:
			return []

		ans = []
		left = intervals[0].start
		right = intervals[0].end
		for x in intervals:
			if x.start <= right:
				right = max(right,x.end)
			else:
				ans.append(Interval(left,right))
				left = x.start
				right = x.end
		ans.append(Interval(left, right))
		return ans



