"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None:
#             return head
#         elif head.next is None:
#             return head
#         else:
#             prev = head
#             node = head.next
#             while(node):
#                 if prev.val == node.val:
#                     prev.next = node.next   
#                     node = prev.next
#                 else:
#                     prev = node
#                     node = node.next
#         return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None:
#             return head
#         elif head.next is None:
#             return head
#         else:
#             prev = head
#             node = head.next
#             while(node):
#                 if prev.val == node.val:
#                     if node.next:
#                         prev.next = node.next
#                         node = prev.next
#                     else:
#                         prev.next = None
#                         break
#                 else:
#                     prev = node
#                     node = node.next
#             return head