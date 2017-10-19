# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 9:36'


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		"""
		intervals.append(newInterval)
		intervals.sort(key= lambda i :i.start)
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




