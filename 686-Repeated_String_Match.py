#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/repeated-string-match/description/
# http://bookshadow.com/weblog/2017/10/01/leetcode-repeated-string-match/

"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
Note:
    The length of A and B will be between 1 and 10000.
"""
class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        sa, sb = len(A), len(B)
        x = 1
        while (x - 1) * sa <= 2 * max(sa, sb):
            if B in A * x : return x
        return -1
