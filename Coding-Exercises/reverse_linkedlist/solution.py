class Solution:
    def reverse(self, head, k):
        if head is None or head.next is None:
            return head
        count = 0
        prev = None
        curr = head
        while curr and count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        if curr:
            head.next = self.reverse(curr, k)
        return prev


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
