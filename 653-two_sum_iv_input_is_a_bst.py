#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: nemo_chen
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# http://bookshadow.com/weblog/2017/08/06/leetcode-two-sum-iv-input-is-a-bst/
'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True
'''
class Solution(object):
    def search(self, node):
        if not node:
            return False
        if node.val not in self.hashmap:
            self.hashmap[self.k - node.val] = node.val
            return (self.search(node.left) or self.search(node.right))
        else:
            return True

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.hashmap = {}
        self.k = k
        return self.search(root)
