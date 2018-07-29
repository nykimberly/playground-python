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


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)
node.next.next.next.next.next.next = ListNode(7)

sol = Solution()
n = sol.reverse(node, 2)

while n:
    print(n.val)
    n = n.next
