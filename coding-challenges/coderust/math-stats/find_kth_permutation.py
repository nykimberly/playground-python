
"""
Given a set of n elements, find the kth permutation
i.e. [1, 2, 3] -> [123, 132, 213, 231, 312, 321]
"""

def permute(n, l, r, p):
    """Use recursion:
    List of n items possess n! permutations
    We find these by "fixing" one character and swapping the remaining
    """
    if l == r:
        p.append("".join(n))
    for i in range(l, r+1):
        n[l], n[i] = n[i], n[l]  # swap
        permute(n, l+1, r, p)
        n[l], n[i] = n[i], n[l]  # unswap


def find_kth_permutation(n, k):
    permutations = []
    permute(n, 0, len(n) - 1, permutations)
    if k <= len(permutations):
        return permutations[k-1]
    else:
        return -1

if __name__ == "__main__":
    n, k = ["a", "b", "c"], 6
    e = ["abc", "acb", "bac", "bca", "cba", "cab"][k-1]
    o = find_kth_permutation(n, k)
    assert o == e, o

    n, k = ["1", "2", "3"], 6
    e = ["123", "132", "213", "231", "321", "312"][k-1]
    o = find_kth_permutation(n, k)
    assert o == e, o

    n, k = ["1", "2", "3", "4"], 8
    e = "2143"
    o = find_kth_permutation(n, k)
    assert o == e, o
    print("Success!")