#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an array of integers, rotate the array by 'N' elements.
"""


def rotate_array(arr, n):
  if n == 0:
    return arr
  elif n < 0:
    return arr[-n:] + arr[:-n]
  else:
    return arr[-n:] + arr[:-n]


if __name__ == "__main__":
    print(rotate_array([1, 2, 3, 4, 5], 2))
    print(rotate_array([1, 2, 3, 4, 5], -3))