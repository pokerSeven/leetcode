# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 9:12'


class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		hei = list(set(height))
		hei.sort()

		re = [0]
		for i,v in enumerate(hei):
			if i != 0:
				d_value = hei[i] - hei[i - 1]
				left = [-1]
				for j , x in enumerate(height):
					if x >= v:
						if left[0] != -1:
							re[0] += (j - left[0] - 1) * d_value
						left[0] = j
		return re[0]

class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""

		max_left = []
		max_right = []

		for i, v in enumerate(height):
			if i == 0:
				max_left.append(v)
			else:
				max_left.append(max(max_left[-1],v))
		for i, v in enumerate(height[::-1]):
			if i == 0:
				max_right.append(v)
			else:
				max_right.append(max(max_right[-1],v))

		max_right = max_right[::-1]

		s = sum(height)
		s1 = [0]
		for i in range(len(height)):
			s1[0] += min(max_right[i],max_left[i])
		return  s1[0] - s



s = Solution()
print s.trap([1,2,1,0])

