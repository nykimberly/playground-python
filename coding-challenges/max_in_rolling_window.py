#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:49:18 2021

@author: kimberlyvnguyen

Given a large array of integers and a window of size w, 
find the current maximum value in the window as the window 
slides through the entire array.
"""

def find_max_sliding_window(arr, window_size):
    result = []
    deck = [0]
    # find initial max
    for i, val in enumerate(arr[:window_size]):
        if val > arr[deck[0]]:
            deck.insert(0, i)
    result.append(arr[deck[0]])
    # now increment, keeping track of max and removing items out of frame
    for i in range(window_size, len(arr)):
        while deck and arr[i] > arr[deck[-1]]:
            deck.pop()
        while deck and deck[0] <= (i - window_size):
            deck.pop(0)
        deck.append(i)
        result.append(arr[deck[0]])
    return result

arr = [1, 2, 3, 4, 3, 2, 1, 2, 5]
print(arr)
ans = find_max_sliding_window(arr,4)
print(ans)