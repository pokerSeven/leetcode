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
        listnum1 = ""
        listnum2 = ""
        while l1 != None:
            listnum1 = str(l1.val) + listnum1
            l1 = l1.next
        while l2 != None:
            listnum2 = str(l2.val) + listnum2
            l2 = l2.next

        value = int(listnum1) + int(listnum2)
        l3 = ListNode(0)
        p = l3
        for x in str(value)[::-1][:-1]:
            l3.val = x
            l3.next = ListNode(None)
            l3 = l3.next
        l3.val = str(value)[0]
        return p