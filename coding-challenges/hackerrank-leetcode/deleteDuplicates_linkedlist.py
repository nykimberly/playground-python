"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            prev = head
            curr = head.next
            while(curr is not None):
                if prev.val == curr.val:
                    if curr.next is not None:
                        prev.next = curr.next
                        curr = prev.next
                    else:
                        prev.next = None
                        break
                else:
                    prev = prev.next
                    curr = curr.next
        return head


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node1.next = node2
node2.next = node3

sol = Solution()

sol.deleteDuplicates(node1)
