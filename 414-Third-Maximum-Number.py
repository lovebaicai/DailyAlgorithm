#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen

# https://leetcode.com/problems/third-maximum-number/description/
# http://bookshadow.com/weblog/2016/10/09/leetcode-third-maximum-number/
"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = NOne
         for n in nums:
            if n > a:
                a, b, c, = n, a, b
            elif a > n > b:
                b, c = n, b
            elif b > n > c:
                c = n
         return c if c is not None else a
