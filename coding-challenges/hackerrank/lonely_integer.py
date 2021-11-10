"""Given an array of integers, where all elements but one occur twice, find the unique element.

lonelyinteger has the following parameter(s):
int a[n]: an array of integers

Returns
int: the element that occurs only once

Approach: Frequency map and return the one with count of 1
"""

import collections
import unittest
import typing


class TestLonelyInteger(unittest.TestCase):
    def test_lonely_integer_fns(self):
        lonely_integer = LonelyInteger()

        def test_lonely_integer(fn: typing.Callable) -> None:
            expected = {(4, 9, 95, 93, 57, 4, 57, 93, 9): 95, (1, 1, 2): 2, (1,): 1}
            for i, expected in expected.items():
                arr = list(i)
                self.assertEqual(expected, fn(arr))

        for fn in lonely_integer.fns:
            test_lonely_integer(fn)


class LonelyInteger:
    def __init__(self) -> None:
        self.fns = [self.lonely_integer, self.lonely_integer_with_counter]

    def lonely_integer(self, arr: typing.List[int]) -> None:
        counter = {}
        for item in arr:
            counter.setdefault(item, 0)
            counter[item] += 1
        for item, count in counter.items():
            if count == 1:
                return item

    def lonely_integer_with_counter(self, arr: typing.List[int]) -> None:
        counter = collections.Counter(arr)
        for k, v in counter.items():
            if v == 1:
                return k
