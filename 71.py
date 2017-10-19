# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 22:11'


class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		left = 0
		for i in range(len(path)):
			if path[i] == "/":
				left = i + 1
			else:
				break

		path = path[left:][::-1]
		left = 0
		for i in range(len(path)):
			if path[i] == "/":
				left = i + 1
			else:
				break
		path = path[left:][::-1]

		ans = []
		ps = path.split("/")
		for n in ps:
			if n == "" or n == ".":
				pass
			elif n == "..":
				ans = ans[:-1]
			else:
				ans.append(n)

		if not ans:
			return "/"
		else:
			re = ""
			for n in ans:
				re = re + "/" + n
			return re




