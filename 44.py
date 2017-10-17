# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/17 10:42'


class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		flag = [True]
		newp = []
		for x in p:
			if x != "*":
				flag[0] = True
				newp.append(x)
			else:
				if flag[0]:
					newp.append(x)
					flag[0] = False
		newp = "".join(newp)
		j = [0]
		for ssub, psub in zip(s, newp):
			if ssub == psub or psub == "?":
				j[0] += 1
			elif psub == "*":
				break
			else:
				return False
		s = s[j[0]:]
		newp = newp[j[0]:]
		j[0] = 0
		for ssub, psub in zip(s[::-1], newp[::-1]):
			if ssub == psub or psub == "?":
				j[0] += 1
			elif psub == "*":
				break
			else:
				return False
		s = s[::-1][j[0]:]
		newp = newp[::-1][j[0]:]
		return self.solve(s, newp)

	def solve(self, s, p):
		if s == p:
			return True
		if not p:
			return False
		if s == "":
			if p[0] == "*":
				return self.isMatch(s, p[1:])
			else:
				return False
		if s[0] == p[0] or p[0] == "?":
			return self.isMatch(s[1:], p[1:])
		if p[0] == "*":
			if self.isMatch(s[1:], p[1:]):
				return True
			if self.isMatch(s[1:], p[:]):
				return True
			if self.isMatch(s[:], p[1:]):
				return True
		return False


class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if s == p:
			return True
		if not p:
			return False
		arr = p.split("*")
		p_list = []
		for x in arr:
			if x != "":
				p_list.append(x)
		if len(p_list) == 0:
			return True

		if p[0] != "*":
			s = "$" + s
			p_list[0] = "$" + p_list[0]
		if p[-1] != "*":
			s = s + "$"
			p_list[-1] = p_list[-1] + "$"
		while len(p_list) != 0:
			index = self.find(s,p_list[0])
			if index == -1:
				return False
			else:
				s = s[index + len(p_list[0]):]
			del p_list[0]
		return True

	def find(self,str, sub):
		for i in range(len(str) - len(sub) + 1):
			for j , v in enumerate(sub):
				if str[i + j] == sub[j] or sub[j] == "?":
					pass
				else:
					break
			else:
				return i
		return -1

s = Solution()
print s.isMatch(
	"b",
"*?*?")
