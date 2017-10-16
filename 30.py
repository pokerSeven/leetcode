# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/15 11:12'


# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).


class Solution(object):
	def findSubstring(self, s, words):
		"""
		:type s: str
		:type words: List[str]
		:rtype: List[int]
		"""
		words_dict = {}
		if not words:
			return []
		word_len = len(words[0])
		for x in words:
			if words_dict.has_key(x):
				words_dict[x] += 1
			else:
				words_dict[x] = 1
		w_dict = {}
		m = [0, -1]
		res = []
		apper_len = [0]
		for i in range(len(s)):
			m[0] = i
			w_dict = {}
			m[1] = -1
			apper_len[0] = 0
			while m[0] < len(s):
				item = s[m[0]:m[0] + word_len]
				if words_dict.has_key(item):
					if not w_dict.has_key(item):
						w_dict[item] = [m[0]]
						apper_len[0] += 1
						if m[1] == -1:
							m[1] = m[0]
					else:
						if len(w_dict[item]) >= words_dict[item]:
							break
						apper_len[0] += 1
						w_dict[item].append(m[0])

					m[0] += word_len
				else:

					break
				if apper_len[0] == len(words):
					res.append(m[1])
					break

		return res


class Solution(object):
	def findSubstring(self, s, words):
		"""
		:type s: str
		:type words: List[str]
		:rtype: List[int]
		"""
		words_dict = {}
		if not words:
			return []
		word_len = len(words[0])
		for x in words:
			if words_dict.has_key(x):
				words_dict[x] += 1
			else:
				words_dict[x] = 1
		w_dict = {}
		m = [0, -1]
		res = []
		apper_len = [0]
		range_list = [1 for x in range (len(s) - len(words)*len(words[0]) + 1)]

		for i in range(len(s) - len(words)*len(words[0]) + 1):
			if range_list[i] != -1:
				m[0] = i
				w_dict = {}
				m[1] = -1
				apper_len[0] = 0
				while m[0] < len(s):
					item = s[m[0]:m[0] + word_len]
					if words_dict.has_key(item):
						if not w_dict.has_key(item):
							w_dict[item] = [m[0]]
							apper_len[0] += 1
							if m[1] == -1:
								m[1] = m[0]
						else:
							if len(w_dict[item]) >= words_dict[item]:
								start = w_dict[item][0]
								m[1] = start +word_len
								if m[1] < len(range_list):
									range_list[m[1]] = -1
								for _,value in w_dict.items():
									for x in value:
										if x <= start:
											apper_len[0] -= 1
											value.remove(x)
											if x < len(range_list):
												range_list[x] = -1

							apper_len[0] += 1
							w_dict[item].append(m[0])

						m[0] += word_len
					else:
						for _, value in w_dict.items():
							for x in value:
								if x < len(range_list):
									range_list[x] = -1
						break

					if apper_len[0] == len(words):
						print w_dict
						res.append(m[1])
						break
		return res

s = Solution()
print s.findSubstring("ababaab",
["ab","ba","ba"])



