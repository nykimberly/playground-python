# -*- coding: utf-8 -*-


# good ol binary search
def binarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False
    while (first <= last) & (not found):
        mid = (first+last)//2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


testlist = [0, 1, 3, 9, 13, 17, 19, 32, 52]
print(binarySearch(testlist, 7))
print(binarySearch(testlist, 32))
