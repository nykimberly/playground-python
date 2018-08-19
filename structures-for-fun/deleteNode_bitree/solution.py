# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    count = 0

    def deleteNode(self, root, key):
        self.count += 1
        print("recursing %d times" % self.count)
        if root is None:
            print("root is none")
            return root
        if key < root.val:
            print("target may be to the left")
            root.left = self.deleteNode(root.left, key)
            print("curr left is ", root.left)
        elif key > root.val:
            print("target may be to the right")
            root.right = self.deleteNode(root.right, key)
            print("curr right is ", root.right)
        else:
            if root.left is None:
                print("target has no left child")
                right = root.right
                print("right child is", right)
                del(root)
                return right
            elif root.right is None:
                print("target has no right child")
                left = root.left
                print("left child is", left)
                del(root)
                return left
            else:
                print("target has children")
                successor = root.right
                while successor.left:
                    successor = successor.left
                print("successor has been identified as", successor.val)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        print("end at root=", root.val)
        return root
