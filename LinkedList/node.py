#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:43:07 2018

@author: nykimberly
"""


class Node:

    def __init__(self, val, next=None):
        self.val = val
        if next is not None:
            assert isinstance(next, Node), \
                "Invalid assignment. \
                Node must point toward another node!"
            self.next = next
        else:
            self.next = next
