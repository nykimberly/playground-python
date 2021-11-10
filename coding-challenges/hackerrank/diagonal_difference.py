"""Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example
1 2 3
4 5 6
9 8 9

Sums are 1+5+9=15 and 2+5+9=17 absolute difference is 2
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
        self.fns = [self.diagonal_difference, self.diagonal_difference_less_space]

    def diagonal_difference(self, arr: typing.List[int]) -> None:
        l = len(arr)
        ld = 0
        rd = 0
        for i in range(l):
            ld += arr[i][i]
            rd += arr[i][l - 1 - i]
        difference = ld - rd
        return difference * -1 if difference < 0 else difference

    def diagonal_difference_less_space(self, arr: typing.List[int]) -> None:
        n = len(arr)
        diff = 0
        for i in range(0, n):
            diff += arr[i][i]
            diff -= arr[i][n - 1 - i]
        return abs(diff)
