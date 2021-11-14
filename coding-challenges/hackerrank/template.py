"""Prompt

Example

Contract
Input Format:
Returns:
Contstraints:
"""


import unittest
import typing


class TestSolution(unittest.TestCase):
    def test_solutions(self):
        solution = Solution()

        def test_solution(fn: typing.Callable) -> None:
            arguments = [
                {
                    "arg": 0
                }
            ]
            expected = [0]
            for i, kwargs in enumerate(arguments):
                self.assertEqual(fn(**kwargs), expected[i])

        for fn in solution.solutions:
            test_solution(fn)


class Solution:
    def __init__(self) -> None:
        self.solutions = [getattr(self, attr) for attr in dir(self) if not attr.startswith("_")]
        assert self.solutions

    @staticmethod
    def solution1(arg: int) -> int:
        return arg
    