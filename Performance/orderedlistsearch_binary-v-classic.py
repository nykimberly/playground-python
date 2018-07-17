# -*- coding: utf-8 -*-
import timeit
import random
import matplotlib.pyplot as plt


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


# classic search for comparison
def iterSearch(list, item):
    for element in list:
        if item == element:
            return True
    return False


binary = timeit.Timer("binarySearch(t, gold)",
                      "from __main__ import binarySearch, t, gold")

classic = timeit.Timer("iterSearch(t, gold)",
                       "from __main__ import iterSearch, t, gold")

# lets plot it
sample = 0
i_arr = []
b_arr = []
c_arr = []

# chart of data
print("Sample | Search | %-15s | %-15s" % ("binary", "classic"))
print("--------------------------------------\n")
# increment from 0 to 1000000 in steps of 50000
for i in range(0, 500000, 2000):
    gold = random.randint(0, i)
    i_arr.append(i)
    t = list(range(i))
    b = binary.timeit(number=1000)
    b_arr.append(b)
    t = list(range(i))
    c = classic.timeit(number=1000)
    c_arr.append(c)
    sample += 1
    print("%-6s | %-6s | %-15.5f | %-15.5f" % (sample, gold, b, c))

# plot of data
plt.scatter(i_arr, b_arr, color='blue', label='Binary')
plt.scatter(i_arr, c_arr, color='red', label='Classic')
plt.grid()
plt.title('Time Complexity: Binary vs. Classic Search')
plt.xlabel('List size')
plt.ylabel('Operation time in milliseconds')
plt.legend()
plt.show()
