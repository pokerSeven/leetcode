# -*- coding: utf-8 -*-
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        class State(object):
            n1 = None
            n2 = None

            def push(self, n):
                self.n1 = self.n2
                self.n2 = n

        state = State()
        index_1 = 0
        index_2 = 0
        len_1 = len(nums1)
        len_2 = len(nums2)
        lens = len_1 + len_2

        for i in range(lens / 2 + 1):
            if index_1 >= len_1:
                state.push(nums2[index_2])
                index_2 = index_2 + 1
            elif index_2 >= len_2:
                state.push(nums1[index_1])
                index_1 = index_1 + 1
            elif nums1[index_1] < nums2[index_2]:
                state.push(nums1[index_1])
                index_1 = index_1 + 1
            else:
                state.push(nums2[index_2])
                index_2 = index_2 + 1
            print state.n1, state.n2

        if lens % 2 == 0:
            return (state.n1 + state.n2) * 1.0 / 2
        else:
            return state.n2


s = Solution()
print s.findMedianSortedArrays([1, 3], [2])
