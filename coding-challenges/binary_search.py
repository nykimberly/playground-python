#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:57:31 2021

@author: kimberlyvnguyen
"""

def binary_search(a, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, key, low, mid-1)
    else:
        return binary_search(a, key, mid+1, high)
    
def binary_search_iter(a, key):
    low = 0
    high = len(a)
    while low <= high:
        mid = (low + high) // 2
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1