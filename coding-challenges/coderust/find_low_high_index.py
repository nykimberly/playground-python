#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a sorted array of integers, 
return the low and high index of the given key.
"""


def find_low_index(arr, n):
    low = 0
    high = len(arr) - 1
    idx = -1
    while low <= high:
        mid = (low + high) // 2
        if n <= arr[mid]:
            if n == arr[mid]:
                idx = mid
            high = mid - 1
        elif n > arr[mid]:
            low = mid + 1
    return idx


def find_high_index(arr, n):
    low = 0
    high = len(arr) - 1
    idx = -1
    while low <= high:
        mid = (low + high) // 2
        if n >= arr[mid]:
            if n == arr[mid]:
                idx = mid
            low = mid + 1
        elif n < arr[mid]:
            high = mid - 1
    return idx


if __name__ == "__main__":
    arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    key = 5
    print(find_low_index(arr, key))
    print(find_high_index(arr, key))
    key = -2
    print(find_low_index(arr, key))
    print(find_high_index(arr, key))