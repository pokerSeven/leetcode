# -*- coding: utf-8 -*-
"""
Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		if len(lists) == 0:
			return None
		if len(lists) == 1:
			return lists[0]
		if len(lists) == 2:
			return self.mergeTwoLists(lists[0], lists[1])
		else:
			l1 = lists[:(len(lists) / 2)]
			l2 = lists[(len(lists) / 2):]
			return self.mergeTwoLists(self.mergeKLists(l1), self.mergeKLists(l2))

	def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		if l1.val < l2.val:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2


class Solution1(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		if len(lists) == 0:
			return None
		result = lists[:]
		while True:
			if len(result) == 1:
				return result[0]
			else:
				temp = result
				result = []
				for i in range(0, len(temp), 2):
					if i + 1 < len(temp):
						result.append(self.mergeTwoLists(temp[i], temp[i + 1]))
					else:
						result.append(self.mergeTwoLists(temp[i], None))

	def mergeTwoLists(self, l1, l2):
		start = ListNode(0)
		p_node = start
		while l1 != None and l2 != None:
			if l1.val < l2.val:
				p_node.next = l1
				p_node = p_node.next
				l1 = l1.next
			else:
				p_node.next = l2
				p_node = p_node.next
				l2 = l2.next

		if  l1 == None:
			p_node.next = l2
		if  l2 == None:
			p_node.next = l1
		return start.next

