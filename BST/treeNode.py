# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def search(self, target):
        if target < self.val:
            #print(self.val)
            if self.left is None:
                print("not found")
                return
            self.left.search(target)
        elif target > self.val:
            #print(self.val)
            if self.right is None:
                print("not found")
                return
            self.right.search(target)
        else:
            return self
