"""
Given two integers: x and y; return x ÷ y without using / (division) or * (multiplication) operators.
"""

def bit_div(dividend, divisor):
    """Use bitwise operators
    Runtime complexity:
    Memory complexity:
    """
    if divisor == 0:
        return -1  # cannot divide by 0
    if dividend < divisor:
        return 0  # floor division so zero if less than 1
    if dividend == divisor:
        return 1  # x/x = 1
    if divisor == 1:
        return dividend  # x/1 = x
    if dividend == 0:
        return 0  # 0/y = 0

    quotient = 1
    curr_val = divisor
    while curr_val < dividend:
        print(quotient, curr_val)
        quotient <<= 1 # bit left shift (multiplies by 2)
        curr_val <<= 1

    diff = (dividend - curr_val)
    if diff == 0 or diff == 1: # we've reached our answer (or within margin)
        return quotient

    if diff < 0:  # we've gone too far
        quotient >>= 1
        curr_val >>= 1
    return quotient + bit_div((dividend - curr_val), divisor)

if __name__ == "__main__":
    x, y = 40, 5
    e = 8
    o = bit_div(40, 5)
    assert o == e, o
    x, y = 40, 4
    e = 10
    o = bit_div(40, 4)
    assert o == e, o
    print("Success!")