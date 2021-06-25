"""
Given two integers: x and y; return x ÷ y without using / (division) or * (multiplication) operators.
"""

def pythagorean_triplets(arr):
    """Use bitwise operators
    Runtime complexity:
    Memory complexity:
    """
    arr_squares = [i**2 for i in arr]
    triplets = []
    for i, a_sq in enumerate(arr_squares):
        for j in range(i + 1, len(arr_squares)):
            b_sq = arr_squares[j]
            c_sq = a_sq + b_sq
            if c_sq in arr_squares:
                triplets.append(
                tuple(
                        sorted(
                            (
                                int(a_sq**(1/2)),
                                int(b_sq**(1/2)),
                                int(c_sq**(1/2))
                            )
                        )
                    )
                )
    return triplets

if __name__ == "__main__":
    i = [3, 1, 4, 6, 5]
    e = [(3, 4, 5)]
    o = pythagorean_triplets(i)
    assert e == o, o
    i = [4, 16, 1, 2, 3, 5, 6, 8, 25, 10]
    e = [(3, 4, 5), (6, 8, 10)]
    o = pythagorean_triplets(i)
    assert e == o, o
    i = [10, 4, 6, 12, 5]
    e = []
    o = pythagorean_triplets(i)
    assert e == o, o
    print("Success")