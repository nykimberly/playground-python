# -*- coding: utf-8 -*-

from solution import *

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node1.next = node2
node2.next = node3

sol = Solution()

print(sol.deleteDuplicates(node1))
