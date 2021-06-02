
from collections import defaultdict

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    """Computes full array w/ operations"""
    arr = [0] * n
    curr_max = 0
    for query in queries:
        [a, b, k] = query
        for i in range(a,b+1):
            idx = i-1
            arr[idx] += k
            if arr[idx] > curr_max:
                curr_max = arr[idx]
    return curr_max

def arrayManipulationOptimized(n, queries):
    """Cumulative sum on array to find max"""
    arr_to_sum = [0] * (n+1)
    curr_max = 0
    for query in queries:
        [a, b, k] = query
        z_idx_a = a-1
        z_idx_b = b-1
        arr_to_sum[z_idx_a] += k
        arr_to_sum[z_idx_b+1] -= k
    curr_sum = 0
    for val in arr_to_sum:
        curr_sum += val
        if curr_sum > curr_max:
            curr_max = curr_sum
    return curr_max


if __name__ == '__main__':
    with open("inputs/arrayManipulation.txt", "r") as f:
        queries = []
        for i, line in enumerate(f):
            if i == 0:
                first_multiple_input = line.rstrip().split()
                n = int(first_multiple_input[0])
                m = int(first_multiple_input[1])
            else:
                queries.append(list(map(int, line.rstrip().split())))
    print(n, m, len(queries))
    result = arrayManipulationOptimized(n, queries)
    print(result)