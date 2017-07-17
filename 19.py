"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

class Solution(object):
    class i_node(object):
        node = None
        n = 0
        def __init__(self,no):
            self.node = no
            self.n = 1
        def pp(self,x):
            if x >self.n:
                self.n += 1
            else:
                self.node = self.node.next
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

