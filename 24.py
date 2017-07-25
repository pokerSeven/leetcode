# -*- coding: utf-8 -*-
"""
Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		start = ListNode(0)
		start.next = head
		p_node = start

		while p_node.next != None and p_node.next.next != None:
			p_next = p_node.next
			p_next_next = p_node.next.next
			p_node.next = p_next_next
			p_next.next = p_next_next.next
			p_next_next.next = p_next
			p_node = p_next

		return start.next

	def swapPairs1(self, head):
		pre, pre.next = self, head
		while pre.next and pre.next.next:
			a = pre.next
			b = a.next
			pre.next, b.next, a.next = b, a, b.next
			pre = a
		return self.next