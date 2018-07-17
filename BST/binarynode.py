#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:43:15 2018

@author: nykimberly
"""

# Implementing some typical bst methods


class binaryNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = binaryNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = binaryNode(val)
            else:
                self.right.insert(val)
