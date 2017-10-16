# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/16 21:38'


class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		if n == 1:
			return "1"
		else:
			re = [""]
			flag = "0"
			num = 0
			for x in self.countAndSay(n-1):
				if flag == x:
					num += 1
				else:
					if flag != "0":
						re[0] = re[0] + str(num)+flag
					flag = x
					num = 1
			re[0] = re[0] + str(num) + flag
			return re[0]

s = Solution()
print s.countAndSay(4)


