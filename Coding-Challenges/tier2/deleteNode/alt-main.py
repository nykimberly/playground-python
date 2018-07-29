from solution import TreeNode, Solution

node = TreeNode(5)
node.left = TreeNode(3)
node.left.left = TreeNode(2)
node.left.left.left = TreeNode(1)
node.left.right = TreeNode(4)
node.right = TreeNode(7)
node.right.left = TreeNode(6)
node.right.right = TreeNode(8)


def printNode(root):
    if root is None:
        return
    printNode(root.left)
    print(root.val)
    printNode(root.right)


printNode(node)
print("=====================")

sol = Solution()
sol.findMin(node)
sol.search(node, 7)