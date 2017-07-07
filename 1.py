# -*- coding: utf-8 -*-
"""
Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index,value in enumerate(nums) :
            expect_value = target - value
            if dict.get(expect_value) is not None:  #不能直接使用dict.get(expect_value)作为判断条件，0也会被认为是False
                return dict[expect_value],index
            else:
                dict[value] = index