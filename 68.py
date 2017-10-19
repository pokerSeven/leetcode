# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 15:59'


class Solution(object):
	def fullJustify(self, words, maxWidth):
		"""
		:type words: List[str]
		:type maxWidth: int
		:rtype: List[str]
		"""
		ans = []
		cur = 0
		temp = []
		tempL = 0
		while True:
			if len(words[cur]) + tempL <= maxWidth:
				temp.append(words[cur])
				tempL = tempL + len(words[cur]) + 1
				cur += 1
			else:
				t = maxWidth - tempL + 1
				le = len(temp) - 1
				print t,le,tempL
				a = ""
				if le == 0:
					a = temp[0].ljust(maxWidth)
				else:
					for s in temp:
						t1 = t / le
						t2 = t % le
						if t2:
							a = a + s + "".ljust(t1 + 2," ")
							t -= 1
						else:
							a = a + s + "".ljust(t1+1," ")
				ans.append(a[:maxWidth])
				temp = []
				tempL = 0
			print cur,ans
			if cur >= len(words):
				if tempL == 0:
					return ans
				else:
					ans.append(" ".join(temp).ljust(maxWidth))
					return ans


s = Solution()
print s.fullJustify(["T", "i", "n", "j"]
					, 1)
