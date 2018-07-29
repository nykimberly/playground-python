# -*- coding: utf-8 -*-

from solution import Solution, Interval

Bnode1 = ListNode(2)
Bnode2 = ListNode(6)
Bnode3 = ListNode(14)
Bnode1.next = Bnode2
Bnode2.next = Bnode3

Anode1 = ListNode(0)
Anode2 = ListNode(2)
Anode3 = ListNode(15)
Anode1.next = Anode2
Anode2.next = Anode3


lst = [Anode1, Bnode1]

sol = Solution()

n = sol.mergeTwoLists(lst[0], lst[1])

while(n):
    print(n.val)
    if n.next:
        n = n.next
    else:
        print("end of node")
        break