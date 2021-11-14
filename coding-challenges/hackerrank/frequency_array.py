"""Prompt
Given a list of integers, count and return the number of times each value appears as an array of integers.

Example
arr = [1, 1, 3, 2, 1]
frequency_arr = [0, 3, 1, 1]

Contract
Input Format:
The first line contains an integer n, the number of items in arr.
Each of the next n lines contains an integer arr[i] where 0 <= i <= n.

Returns:
int[100]: a frequency array

Contstraints:
100 <= n <= 10e6
0 <= arr[i] < 100
"""


import unittest
import typing


class TestSolution(unittest.TestCase):
    def test_solutions(self):
        solution = Solution()

        def test_solution(fn: typing.Callable) -> None:
            arguments = [
                {
                    "n": 100,
                    "arr": [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]
                }
            ]
            expected = [[0, 2, 0, 2, 0, 0, 1, 0, 1, 2, 1, 0, 1, 1, 0, 0, 2, 0, 1, 0, 1, 2, 1, 1, 1, 3, 0, 2, 0, 0, 2, 0, 3, 3, 1, 0, 0, 0, 0, 2, 2, 1, 1, 1, 2, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 3, 2, 0, 0, 2, 1, 2, 1, 0, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 0, 3, 2, 1, 1, 0, 1, 1, 1, 0, 2, 2]]
            for i, kwargs in enumerate(arguments):
                self.assertEqual(fn(**kwargs), expected[i])

        for fn in solution.solutions:
            test_solution(fn)


class Solution:
    def __init__(self) -> None:
        self.solutions = [getattr(self, attr) for attr in dir(self) if not attr.startswith("_")]
        assert self.solutions

    @staticmethod
    def frequency_arrary(n: int, arr: typing.List[int]) -> None:
        freq_arr = [0] * 100
        for val in arr:
            freq_arr[val] += 1
        return freq_arr