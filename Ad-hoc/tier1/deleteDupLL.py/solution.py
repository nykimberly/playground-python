"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        elif head.next is None:
            return head
        else:
            prev = head
            node = head.next
            while(node):
                if prev.val == node.val:
                    prev.next = node.next   
                    node = prev.next
                else:
                    prev = node
                    node = node.next
        return head