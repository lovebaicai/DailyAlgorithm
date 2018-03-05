#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: nemo_chen

# https://leetcode.com/problems/invert-binary-tree/description/ 
# http://bookshadow.com/weblog/2015/06/12/leetcode-invert-binary-tree/

'''
Invert a binary tree.
        4
      /   \
     2     7
    / \   / \
   1   3 6   9

to
        4
      /   \
     7     2
    / \   / \
   9   6 3   1
'''

def Solution(object):
    def invertTree(self, root):
        """
        type root: TreeNone
        rtype: TreeNone
        """
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

