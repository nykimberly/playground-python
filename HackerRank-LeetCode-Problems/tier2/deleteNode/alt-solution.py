# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findMin(self, root):
        if root.left is not None:
            self.findMin(root.left)
        else:
            self.min = root
            print("Found min val of", self.min.val)
            return self.min

    def search(self, root, key):
        if key < root.val:
            if root.left is not None:
                print("Curr root is %d, searching left" % root.val)
                self.search(root.left, key)
            else:
                print("Not found")
                return
        elif key > root.val:
            if root.left is not None:
                print("Curr root is %d, searching right" % root.val)
                self.search(root.right, key)
            else:
                print("Not found")
        else:
            self.searchTarget = root
            print("Found! Returning root for", self.searchTarget.val)
            return self.searchTarget
