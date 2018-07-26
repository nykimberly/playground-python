#!/bin/python3

import os
'''
Input:
5 4
1 2 3 4 5

Output:
5 1 2 3 4
'''
# Complete the rotLeft function below.


def rotLeft(a, d):
    res = [0]*len(a)
    for i, e in enumerate(a):
        index = (i - d) % len(a)
        res[index] = e
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
