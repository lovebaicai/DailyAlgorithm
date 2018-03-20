#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/perfect-number/description/
# http://bookshadow.com/weblog/2017/03/26/leetcode-perfect-number/
'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14
    Note: The input number n will not exceed 100,000,000. (1e8)
'''

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num == 1: return False
        x = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                x += i
                x += num / i
        return (x - num) == num
