# -*- coding: utf-8 -*-

from solution import Solution, ListNode

Anode1 = ListNode(1)
Anode2 = ListNode(4)
Anode3 = ListNode(5)
Anode1.next = Anode2
Anode2.next = Anode3
Bnode1 = ListNode(1)
Bnode2 = ListNode(3)
Bnode3 = ListNode(4)
Bnode1.next = Bnode2
Bnode2.next = Bnode3
Cnode1 = ListNode(2)
Cnode2 = ListNode(6)
Cnode1.next = Cnode2

lst = [Anode1, Bnode1, Cnode1]

sol = Solution()

print(sol.mergeKLists(lst))
