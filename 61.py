# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/18 11:40'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if k == 0:
			return head
		tail = head
		nodeList = []
		while tail != None:
			nodeList.append(tail)
			tail = tail.next

		k = k % len(nodeList)
		nodeList = nodeList[k:]+nodeList[:k]
		nodeList.append(None)
		for i in range(len(nodeList)-1):
			nodeList[i].next = nodeList[i+1]

		return nodeList[0]





