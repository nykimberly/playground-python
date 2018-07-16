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


'''
Sample input: 1 3 5 2 4 6 8
Sample output: 3
'''

r = list(map(int, input("please provide input: ").rsplit()))
minimumSwaps(r)
