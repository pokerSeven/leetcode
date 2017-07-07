# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        listnum1 = []
        listnum2 = []
        while l1 != None:
            listnum1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            listnum2.append(l2.val)
            l2 = l2.next

        value_1 = reduce((lambda x1, x2: 10 * x1 + x2), listnum1)
        value_2 = reduce(lambda x1, x2: 10 * x1 + x2, listnum2)
        value = value_1 + value_2
        l3 = ListNode(0)
        p = ListNode(0)
        p = l3
        for x in map(int, str(value))[::-1][:-1]:
            l3.val = x
            l3.next = temp = ListNode(None)
            l3 = l3.next
        l3.val = int(str(value)[0])
        return p

