# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        for k in lists:
            node = k
            while(node):
                print(node.val)
                if node.next:
                    node = node.next
                else:
                    print("end of node")
                    break

class Solution(object):
    def mergeTwoLists(self, n1, n2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        soln = tail = ListNode(0)
        while(n1 and n2):
            if n1.val <= n2.val:
                prev = n1
                n1 = n1.next
            else:
                prev = n2
                n2 = n2.next
            tail.next = prev
            tail = tail.next
        tail.next = n1 or n2
        return soln.next