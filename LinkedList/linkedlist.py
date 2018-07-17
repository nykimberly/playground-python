#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:43:15 2018

@author: nykimberly
"""

from node import Node

# Implementing some typical ll methods


class LinkedList:

    # Initialize linked list with head=>None
    def __init__(self):
        self.head = None

    # Return head of linked list
    def getFirst(self):
        return self.head

    # Create node pointing to old head
    # Reassign new head to this node
    def insertFirst(self, val):
        self.head = Node(val, self.head)

    # Point over the original 1st toward the 2nd
    def removeFirst(self):
        if self.head.next:
            self.head = self.head.next
        # If no other element then point head to none
        else:
            self.head = None

    # Walk across list to get size
    # If no next node then size is 0
    def getSize(self):
        if self.head is None:
            return 0
        else:
            count = 0
            node = self.head
            while(node.next):
                count += 1
                node = node.next
            return count + 1

    # Grab last node
    def getLast(self):
        # Provide error if list is empty
        assert self.head is not None, \
            "Last node unavailable... List is empty!"
        node = self.head
        while(node.next):
            node = node.next
        return node

    # Grab last node and point to new val
    def insertLast(self, val):
        last = self.getLast()
        if last:
            last.next = Node(val)
        # If list is empty, then add to head
        else:
            self.head = Node(val)

    def removeLast(self):
        # If there are no elements, assert error
        assert self.head is not None, \
            "Cannot remove last element... List is empty!"
        # If there is only one element, disconnect head
        if self.head.next is None:
            self.head = None
        # Otherwise, walk through list until second to last element
        else:
            prev = self.head
            node = prev.next
            while(node.next):
                prev = node
                node = node.next
            # disconnect from last element
            prev.next = None

    def clear(self):
        self.head = None
