#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/beautiful-arrangement/description/
# http://bookshadow.com/weblog/2017/02/19/leetcode-beautiful-arrangement/

"""
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
"""

# method one
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = dict()
        def solve(idx, nums):
            if not nums: return 1    
            key = idx, tuple(nums)
            if key in cache: return cache[key]
            ans = 0
            for i, n in enumerate(nums):
                if n % idx == 0 or idx % n == 0:
                    ans += solve(idx + 1, nums[:i] + nums[i+1:])
            cache[key] = ans
            return ans
        return slove(1, range(1, N + 1))

#method two
class Solution(object):
    def countArrangement(self, N):
        self.res = 0
        l = list(range(1, N+1))

        def dfs(rest):
            if len(rest) == 0:
                self.res += 1
                return 
            position = N - len(rest) + 1
            for i in range(len(rest)):
                if position % rest[i] == 0 or rest[i] % position == 0:
                    temp = rest[0:i] + rest[i+1:len(rest)]
                    dfs(temp)
        dsf(l)
        return self.res

