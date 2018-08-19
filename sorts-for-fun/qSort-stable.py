def qSort(arr):
    s = 0
    e = len(arr) - 1
    qSortHelp(arr, s, e)
    return arr


def qSortHelp(arr, start, end):
    if start >= end:
        return
    pivot_index = partition(arr, start, end)
    qSortHelp(arr, start, pivot_index - 1)
    qSortHelp(arr, pivot_index + 1, end)


def partition(arr, start, end):
    p_v = arr[start]
    p_i = start
    l = start
    r = p_i + 1
    curr = start
    while curr <= end:
        if arr[curr] >= p_v:
            r += 1
        else:
            arr[:] = arr[:l] + [arr[curr]] + arr[p_i:curr] + arr[curr+1:]
            p_i += 1
            l += 1
            r += 1
        curr += 1
    return p_i


nums = [10, 30, 11, 5, 0, 30, 1]
print(qSort(nums))
