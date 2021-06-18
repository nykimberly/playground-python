#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from array import array


"""
Remove duplicate characters from a string which is passed by reference.
"""

def remove_duplicates(list_str):
    charset = set()
    write_pos = 0
    for char in list_str:
        if char not in charset:
            charset.add(char)
            list_str[write_pos] = char
            write_pos += 1
    for i in range(write_pos, len(list_str)):
        list_str[i] = "\0"


def getArray(t):
  s = array('u', t)
  return s


if __name__ == "__main__":
    s = getArray("dabbac")
    print("".join(s))
    remove_duplicates(s)
    print("".join(s))