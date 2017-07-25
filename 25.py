# -*- coding: utf-8 -*-
"""
 Reverse Nodes in k-Group
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.
For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		pre, pre.next = self, head

		while True:
			k_nodes = []
			p = pre
			for i in range(k):
				if p and p.next:
					k_nodes.append(p.next)
					p = p.next
				else:
					return self.next
			tail = p.next

			p = pre
			for node in k_nodes[::-1]:
				p.next = node
				p = node
			pre = p
			p.next = tail



