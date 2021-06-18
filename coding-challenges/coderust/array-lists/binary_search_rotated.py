#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


from collections import deque

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
            return -1
    return -1

def random_sorted_list():
    return sorted({
        random.randint(0, 100)
        for _i in range(random.randint(10, 50))
    })

def random_rotate_list(alist):
    alist = deque(alist)
    alist.rotate(random.randint(0, random.randint(0, len(alist))))
    return list(alist)
    
if __name__ == "__main__":
    for _i in range(100):
        arr = random_rotate_list(random_sorted_list())
        key = random.choice(arr)
        result = binary_search_rotated(arr, key)
        expected = arr.index(key) if key in arr else -1
        if result == expected:
            continue
        else:
            print("answer:", result, "expected: ", expected)
            print("input array", arr, "key", key)
            quit()
    print("Passed")
            
