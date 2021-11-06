"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Input
n: int  # size of array
list_n: List[int]  # list of integers

Output
ratio_p
ratio_n
ratio_0
"""

from typing import Any, Dict, List


def plus_minus(list_n: List[int]) -> str:
    t = len(list_n)
    p = n = z = 0
    for val in list_n:
        if val > 0:
            p += 1
        elif val == 0:
            z += 1
        else:
            n += 1
    return f"%.6f\n%.6f\n%.6f" % (p/t, n/t, z/t)
        
def test_cases() -> None:
    list_inputs = [{"list_n": [-4, 3, -9, 0, 4, 1]}]
    expected = [f"0.500000\n0.333333\n0.166667"]
    fails = 0
    for i, inputs in enumerate(list_inputs):
        result = plus_minus(**inputs)
        if result != expected[i]:
            print(f"Got {result}, Expected {expected[i]}")
            fails += 1
    print(f"Tests Failed: {fails}") if fails else print("All passed!")


if __name__ == "__main__":
    test_cases()

    response = input("Do you want to try? y/n")
    if response.lower() == "n":
        exit()

    list_n = list(map(int, input("Enter space delimited values to identify ratios for").split()))
    print(plus_minus(n, list_n))





