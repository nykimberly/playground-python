"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Inputs:
arr = [1, 3, 5, 7, 9]

Output:
16 24
"""

from typing import List


def min_max_sum(r: int, arr: List[int]) -> None:
    """Since we're summing, order doesn't matter. 
    And because we are selecting four of the five, 
    we can just pick four in a row and rotate 
    around the array to cover all combinations.
    arr[:0] + arr[1:]
    arr[:1] + arr[2:]
    arr[:2] + arr[3:]
    Complexity: 2n
    """
    min = float("inf")
    max = float("-inf")
    for i in range(len(arr)):
        val = sum(arr[:i] + arr[i+1:])
        if val < min:
            min = val
        if val > max:
            max = val
    print(min, max)

def min_max_sum2(r: int, arr: List[int]) -> None:
    """Sort ascending and sum left side for min.
    Complexity: nlog(n) due to sorting
    """
    arr.sort()
    print(sum(arr[:4]), sum(arr[1:]))

def min_max_sum3(r: int, arr: List[int]) -> None:
    """Subtract max val from sum for min.
    Complexity: n
    """
    min_ = arr[0]
    max_ = arr[0]
    sum_ = 0
    for i in arr:
        sum_ += i
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    print(sum_ - max_, sum_ - min_)


if __name__ == '__main__':
    arr = [1 2 3 4 5]
    min_max_sum(arr) # 10 14
