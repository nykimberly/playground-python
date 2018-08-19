#Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

import os


def hourglassSum(arr):
    maxSum = float('-inf')
    hg_matrix = 3
    for r in range(len(arr)-hg_matrix+1):
        for c in range(len(arr)-hg_matrix+1):
            currSum = sum(arr[r][c:c+3])\
                    + arr[r+1][c+1]\
                    + sum(arr[r+2][c:c+3])
            print(currSum)
            if currSum > maxSum:
                maxSum = currSum
    return maxSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
