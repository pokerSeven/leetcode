# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 10:13'


class Solution(object):
	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		nums = [x for x in range(1,n+1)]
		factList = [1 for x in range(n)]
		for i in range(1,n):

			factList[i] = factList[i-1] * i
		factList = factList[::-1]
		print factList
		ans = ""
		k -= 1
		for i in range(n):
			if k == 0:
				ans += "".join(map(str,nums))
				return ans
			m = k / factList[i]
			k = k % factList[i]
			ans += str(nums[m ])
			del nums[m]



s = Solution()
print s.getPermutation(3, 5)
