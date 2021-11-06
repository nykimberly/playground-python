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
def linearSearch(list, item):
    for element in list:
        if item == element:
            return True
    return False


binary = timeit.Timer("binarySearch(t, gold)",
                      "from __main__ import binarySearch, t, gold")

linear = timeit.Timer("linearSearch(t, gold)",
                       "from __main__ import linearSearch, t, gold")

# lets plot it
sample = 0
i_arr = []
b_arr = []
l_arr = []

# chart of data
print("Sample | Search | %-15s | %-15s" % ("Binary", "Linear"))
print("--------------------------------------\n")
# increment from 0 to 500000 in steps of 2000
for i in range(0, 100, 1):
    # Comment this in if you want random searches
    # gold = random.randint(0, i)
    # Comment this in if you want worst case
    gold = i
    i_arr.append(i)
    t = list(range(i))
    b = binary.timeit(number=1)
    b_arr.append(b)
    t = list(range(i))
    l = linear.timeit(number=1)
    l_arr.append(l)
    sample += 1
    print("%-6s | %-6s | %-15.5f | %-15.5f" % (sample, gold, b, l))

# plot of data
plt.scatter(i_arr, l_arr, color='red', label='Linear')
plt.scatter(i_arr, b_arr, color='blue', label='Binary')
plt.ylim(-.000001, 0.000035)
plt.grid()
plt.title('Time Complexity: Binary vs. Linear Search')
plt.xlabel('List size')
plt.ylabel('Operation time in hundred-milliseconds')
plt.legend()
plt.show()
