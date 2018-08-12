from binarynode import binaryNode

# building a binary search tree
print("level 0 ====================")
# create root of val 3
root = binaryNode(3)
print("root is ", root)   # ==> 3
print("level 1 ====================")
# insert value lower than root
root.insert(1)
# insert value higher than root
root.insert(7)
# see that 1 has gone to left and 7 has gone to the right
print("left of root is ", root.left)   # ==> 1
print("right of root is ", root.right)  # ==> 7
print("level 2 ====================")
root.insert(5)
root.insert(9)
print("left left of root is ", root.left.left)   # ==> None
print("left right of root is ", root.left.right)  # ==> None
print("right left of root is ", root.right.left)   # ==> 5
print("right right of root is ", root.right.right)  # ==> 9


# iterative strategy for printing lvl by lvl
def bfTraversal(r):
    curlvl = [r]
    while curlvl:
        print(' '.join(str(n.val) for n in curlvl))
        nextlvl = list()
        for node in curlvl:
            if node.left:
                nextlvl.append(node.left)
            if node.right:
                nextlvl.append(node.right)
            curlvl = nextlvl
    return


bfTraversal(root)


# recursive strategy for printing left-root-right
def inorderTraversal(r):
    # base case to stop when r is None
    if r is None:
        return
    # travel left-most first
    inorderTraversal(r.left)
    # then print
    print(r.val)
    # travel right w recursion s.t. left leaves of nodes print 1st
    inorderTraversal(r.right)


print("in order traversal")
inorderTraversal(root)


# recursive strategy for printing root-left-right
def preorderTraversal(r):
    # base case to stop when r is None
    if r is None:
        return
    # print root val first
    print(r.val)
    # then travel left, printing root val first
    preorderTraversal(r.left)
    # then travel right, printing root val first
    preorderTraversal(r.right)


print("pre order traversal")
preorderTraversal(root)
