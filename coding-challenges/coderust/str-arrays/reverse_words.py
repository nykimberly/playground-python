#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from array import array


"""
Remove duplicate characters from a string which is passed by reference.
"""

def reverse_chars(arr_str):
    for i in range(len(arr_str) // 2):
        tmp = arr_str[i]
        arr_str[i] = arr_str[-i-1]
        arr_str[-i-1] = tmp

def reverse_words(arr_str):
    start = 0
    reverse_chars(arr_str)
    for i in range(len(arr_str) + 1):
        if  i == (len(arr_str)) or arr_str[i] == " ":
            for j in range(start, (start + i) // 2):
                step = j - start
                tmp = arr_str[j]
                arr_str[j] = arr_str[i-step-1]
                arr_str[i-step-1] = tmp
            start = i + 1


def get_array(t):
  s = array('u', t)
  return s


if __name__ == "__main__":
    s = get_array('Hello World!')
    print("".join(s))
    reverse_words(s)
    print("".join(s))