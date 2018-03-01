#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/group-anagrams/description/
# https://www.jianshu.com/p/92abcf6839cd

'''
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:[["ate", "eat","tea"],["nat","tan"],["bat”]].Note: All inputs will be in lower-case."]]
'''

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        #type strs = List
        hashmap = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            hashmap[key].append(s)
        return [hashmap[key] for key in hashmap]

