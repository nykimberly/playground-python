#You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

import os


# first iteration, doesn't account for missing elements
def minSwaps(arr):
    print("our argument array is ", arr)
    swap = 0
    for i, element in enumerate(arr):
        while arr[i] != (i+1):
            if arr[i] - (i+1) != 0:
                print("we need to swap element at position %d" % (i+1))
                swap_val = arr[i] - (i+1)
                print("we need to swap by %d" % swap_val)
                arr[i], arr[i + swap_val] = arr[i + swap_val], arr[i]
                swap += 1
                print("arg array is now ", arr)
    print(swap)
    return


# second iteration, accounts for array with missing integers
def minimumSwaps(arr):
    swaps = 0
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        while arr[i] != sorted_arr[i]:
            swap_val = arr[i] - sorted_arr[i]
            arr[i], arr[i + swap_val] = arr[i + swap_val], arr[i]
            swaps += 1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
