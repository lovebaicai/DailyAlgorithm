#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/next-greater-element-ii/description/
# http://bookshadow.com/weblog/2017/02/05/leetcode-next-greater-element-ii/
'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn’t exist, output -1 for this number.
Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1’s next greater number is 2; 
The number 2 can’t find next greater number; 
The second 1’s next greater number needs to search circularly, which is also 2.
'''

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [-1]*len(nums)
        idx = list(range(len(nums)))*2
        for i in idx:
            while (stack and nums[stack[-1]] < nums[i]):
                result[stack.pop()] = nums[i]
            stack.append((i))
        return result
