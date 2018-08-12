def qSort(arr):
    s = 0
    e = len(arr) - 1
    qSortHelp(arr, s, e)


def qSortHelp(array, start, end):
    if start >= end:
        return
    pivot_index = partition(array, start, end)
    qSortHelp(array, start, pivot_index - 1)
    qSortHelp(array, pivot_index + 1, end)


def partition(array, start, end):
    pivot_val = array[start]
    less_p = start + 1
    greater_p = end

    while less_p <= greater_p:
        if array[less_p] <= pivot_val:
            less_p += 1
        else:
            array[less_p], array[greater_p] = array[greater_p], array[less_p]
            greater_p -= 1

    array[start], array[less_p-1] = array[less_p-1], array[start]
    return less_p-1


nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(nums)
qSort(nums)
print(nums)
print(sorted(nums))
