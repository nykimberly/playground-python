#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:49:18 2021

@author: kimberlyvnguyen

Search for a given number in a sorted array, with unique elements, 
that has been rotated by some arbitrary number. 
Return -1 if the number does not exist.
"""

def binary_search_rotated(arr, key):
    """Returns index of key in once-rotated array, if found.

    Implementation Note: Because arr is only rotated once, so at least one of
    the halves is sorted correctly, and so if the key is within that range, 
    check there; otherwise, check the unsorted range.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[low] < arr[mid] and arr[low] <= key and arr[mid] >= key:
            high = mid - 1
        elif arr[mid] < arr[high] and arr[mid] <= key and arr[high] >= key:
            low = mid + 1
        elif arr[low] > arr[mid]:
            high = mid - 1
        elif arr[mid] > arr[high]:
            low = mid + 1
        else:
            print("other condition")
    return -1

v1 = [6, 7, 1, 2, 3, 4, 5]
print("Key(3) found at: " + str(binary_search_rotated(v1, 3)))
print("Key(6) found at: " + str(binary_search_rotated(v1, 6))) 