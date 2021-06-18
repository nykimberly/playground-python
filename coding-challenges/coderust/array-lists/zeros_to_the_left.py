"""
Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in the array. The array has to be modified in-place.
"""

def zeros_to_the_left(alist):
    """Use r/w pointers and go in reverse, so we can fill in zeros last
    Runtime: O(n)
    Space: O(1)
    """
    r = w = len(alist) - 1
    nz = 0
    while w > -1:
        if w < nz:
            alist[w] = 0
            w -= 1
            continue
        if alist[r] == 0:
            r -= 1
            nz += 1
        else:
            alist[w] = alist[r]
            r -= 1
            w -= 1
    return alist


def zeros_to_the_left_alt(i):
    """Use r/w pointers and go in reverse, so we can fill in zeros last
    Runtime: O(n)
    Space: O(1)
    """
    r = w = len(i) - 1
    while w > 0:
        if r < 0:
            i[:w+1] = [0] * (w+1)
            w -= (w+1)
            break
        if i[r] != 0:
            i[w] = i[r]
            w -= 1
        r -= 1
    return i


if __name__ == "__main__":
    i = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    o = zeros_to_the_left_alt(i) 
    e = [0, 0, 0, 1, 10, 20, 59, 63, 88]
    assert o == e, f"Output returned is incorrect: got {o}; expected {e}"
    print("Success!")