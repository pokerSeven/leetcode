# -*- coding: utf-8 -*-
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1 == None and l2 == None:
			return None

		result = None
		temp = None
		if l1 == None:
			result = l2
			temp = result
			l2 = l2.next
		elif l2 == None:
			result = l1
			temp = result
			l1 = l1.next
		elif l1.val > l2.val:
			result = l2
			temp = result
			l2 = l2.next
		else:
			result = l1
			temp = result
			l1 = l1.next

		while l1 != None or l2 != None:
			if l1 == None:
				temp.next = l2
				temp = temp.next
				l2 = l2.next
			elif l2 == None:
				temp.next = l1
				temp = temp.next
				l1 = l1.next
			elif l1.val > l2.val:
				temp.next = l2
				temp = temp.next
				l2 = l2.next
			else:
				temp.next = l1
				temp = temp.next
				l1 = l1.next
		return result


class Solution1(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
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
