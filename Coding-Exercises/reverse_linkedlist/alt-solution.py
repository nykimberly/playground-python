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
        if temp:
            head.next = self.reverse(temp, k)
        return prev