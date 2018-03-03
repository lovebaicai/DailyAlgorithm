#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/remove-element/
# http://blog.csdn.net/qq508618087/article/details/50411731
'''
Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn’t matter what you leave beyond the new length.
Example:Given nums = [3,2,2,3], val = 3,Your function should return length = 2, with the first two elements of nums being 2.
'''

class Solution(object):
    def removeElement(self, nums, val):
        '''
        type nums: List[int]
        type val: int
        '''
        ptr1, ptr2 = 0, 0
        while ptr2 < len(nums):
            if nums[ptr2] != val:
                nums[ptr1] = nums[[ptr2]]
                ptr1 += 1
            ptr2 += 1
        return ptr1
