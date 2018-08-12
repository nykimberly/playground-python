# -*- coding: utf-8 -*-

from hourglass import Hourglass

arr = [
       [-9, -9, -9, 1, 1, 1],
       [0, -9, 0, 4, 3, 2],
       [-9, -9, -9, 1, 2, 3],
       [0, 0, 8, 6, 6, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, 1, 2, 4, 0]
      ]

hg1 = Hourglass(arr)
print("hourglass sums in array are, ", hg1.sums())
print("max sum is ", hg1.maxSum())
