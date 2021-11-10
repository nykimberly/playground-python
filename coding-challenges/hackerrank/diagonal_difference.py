"""Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example
1 2 3
4 5 6
9 8 9

Sums are 1+5+9=15 and 2+5+9=17 absolute difference is 2
"""
"""Given an array of integers, where all elements but one occur twice, find the unique element.

lonelyinteger has the following parameter(s):
int a[n]: an array of integers

Returns
int: the element that occurs only once

Approach: Frequency map and return the one with count of 1
"""

import unittest
import typing


class TestDiagonalDifference(unittest.TestCase):
    def test_fns(self):
        solution = Solution()

        def test_fn(fn: typing.Callable) -> None:
            arguments = [
                {"arr": [[1, 2, 3, 0], [4, 5, 6, 0], [9, 8, 9, 0], [0, 0, 0, 0]]},
                {"arr": [[11, 2, 4], [4, 5, 6], [10, 8, -12]]},
            ]
            expected = [1, 15]
            for i, kwargs in enumerate(arguments):
                self.assertEqual(fn(**kwargs), expected[i])

        for fn in solution.fns:
            test_fn(fn)


class Solution:
    def __init__(self) -> None:
        self.fns = [self.diagonal_difference]

    def diagonal_difference(self, arr: typing.List[int]) -> None:
        l = len(arr)
        ld = 0
        rd = 0
        for i in range(l):
            ld += arr[i][i]
            rd += arr[i][l - 1 - i]
        difference = ld - rd
        return difference * -1 if difference < 0 else difference
