#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given three integer arrays sorted in ascending order, return the smallest number that is common in all three arrays.
"""

def find_least_common_number(arr1, arr2, arr3):
    curr_max = 0
    while arr1 and arr2 and arr3:
        if arr1[0] == arr2[0] and arr2[0] == arr3[0]:
            return arr1[0]
        else:
            curr_max = max(arr1[0], arr2[0], arr3[0])
            if arr1[0] < curr_max:
                arr1.pop(0)
            if arr2[0] < curr_max:
                arr2.pop(0)
            if arr3[0] < curr_max:
                arr3.pop(0)
    return -1

v1 = [6, 7, 10, 25, 30, 63, 64]
v2 = [1, 4, 5, 6, 7, 8, 50]
v3 = [1, 6, 10, 14]

result = find_least_common_number(v1, v2, v3)
print("Least Common Number: " + str(result))