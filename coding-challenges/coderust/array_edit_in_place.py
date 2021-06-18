#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from array import array


"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
"""

WHITESPACES = {" ", "\t"}

def remove_white_spaces(s):
   if s is None or len(s) == 0 or s[0] == "\0":
      return s

   r = 0
   w = 0
   while r < len(s):
      if s[r] in WHITESPACES:
         r += 1
      else:
         s[w] = s[r]
         r += 1
         w += 1
   return s


def to_array(s):
    return array("u", s)


if __name__ == "__main__":
    from guppy import hpy
    h = hpy()
    print(h.heap())
    assert(remove_white_spaces(to_array("    hello world")) == "helloworld")
    s = "\thello world"
    remove_white_spaces(to_array(s))
    assert(s == "helloworld")
    print("Success")
    print(h.heap())
