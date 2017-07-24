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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        slow = start
        fast = start
        for i in range(n + 1):
            fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return start.next


class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        self.pre_node = None
        self.node = head
        self.w = 0
        self.p_node = head
        while self.p_node != None:
            if self.w < n:
                self.w += 1
            else:
                self.pre_node = self.node
                self.node = self.node.next
            self.p_node = self.p_node.next
        if self.node != head:
            self.pre_node.next = self.pre_node.next.next
            return head
        else:
            return head.next


