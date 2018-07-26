# -*- coding: utf-8 -*-
"""
def alternatingCharacters(s):
    a = 0
    b = 0
    for char in s:
        if char == "A":
            a += 1
        elif char == "B":
            b += 1
        else:
            print("A & B's only please!")
    if abs(a-b) == 1 or a-b == 0:
        return 0
    else:
        return abs(a-b)-1
"""

def alternatingCharacters(s):
    i = 0
    deleteCount = 0
    while i < len(s)-1:
        print(s[i])
        if s[i] == s[i+1]:
            deleteCount += 1
            i += 1
        else:
            i += 1
    return deleteCount

alternatingCharacters("AAABBB")