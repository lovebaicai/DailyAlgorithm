#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/water-and-jug-problem/
# http://bookshadow.com/weblog/2016/06/24/leetcode-water-and-jug-problem/
"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. 
You need to determine whether it is possible to measure exactly z litres using these two jugs.
If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
Operations allowed:
    Fill any of the jugs completely with water.
    Empty any of the jugs.
    Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
    Example 1: (From the famous "Die Hard" example)
    Input: x = 3, y = 5, z = 4
    Output: True
"""

class Solution(object):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    def canMeasureWater(self, x, y, z):
        vis = set()
        vis.add(0)
        queue = [0]

        while len(queue) > 0:
            q = queue.pop()
            if q == z:
                return True
            qt = []
            if q >= x:
                qt.append(q-x)
            if q >= y:
                qt.append(q-y)
            if q <= x:
                qt.append(q+y)
            if q <= y:
                qt.append(q+x)
            for i in qt:
                if i not in vis:
                    queue.append(i)
                    vis.add(i)
        return False


