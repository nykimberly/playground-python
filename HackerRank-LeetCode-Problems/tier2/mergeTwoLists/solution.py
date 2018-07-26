# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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
"""
class Solution(object):
    def mergeTwoLists(self, n1, n2):
        curr1 = n1
        curr2 = n2
        while(curr1 or curr2):
            if curr1.val < curr2.val:
                if curr1.next:
                    if curr1.next.val > curr2.val:
                        temp1 = curr1.next
                        temp2 = curr2.next
                        curr1.next = curr2
                        curr2.next = temp1
                        curr1 = temp1
                        curr2 = temp2
                    else:
                        curr1 = curr1.next
                else:
                    curr1.next = curr2
                    print("ending logic 1")
                    return n1
            else:
                if curr2.next:
                    if curr2.next.val > curr1.val:
                        temp1 = curr1.next
                        temp2 = curr2.next
                        curr2.next = curr1
                        curr1.next = temp2
                        curr1 = temp1
                        curr2 = temp2
                    else:
                        curr2 = curr2.next
                else:
                    curr2.next = curr1
                    print("ending logic 2")
                    return n2
        print("ending logic 3")
"""