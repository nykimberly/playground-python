#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from array import array


"""
Given a null terminated string, remove any white spaces (tabs or spaces). For example:

All greek to me.
After removing the white spaces, the string should look like this:

Allgreektome.
"""

WHITESPACES = {" ", "\t"}

def remove_white_spaces(s):
    """Use read and write pointers.

    Runtime: O(n)
    Memory: O(1)

    https://www.educative.io/courses/coderust-hacking-the-coding-interview/mqy0
    """
    # Early exit conditions
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

def to_str(sarr):
    return "".join(sarr)


if __name__ == "__main__":
    # Checks that we return expected answer
    output = to_str(remove_white_spaces(to_array("    hello world")))
    assert(output == "helloworld", output)

    # Checks that we edited string (array) in place
    s = "\thello world"
    to_str(remove_white_spaces(to_array(s)))
    assert(s == "helloworld", s)
