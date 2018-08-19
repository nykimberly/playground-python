#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it.

import timeit
import matplotlib.pyplot as plt


def firstGet(rowIndex):
    soln = [1]
    for i in range(1, rowIndex + 1):
        output = [1]
        for j in range(1, i + 1):
            if (j == i):
                val = 1
            else:
                val = soln[i-1][j-1] + soln[i-1][j]
            output.append(val)
        soln.append(output)
    return soln[rowIndex]


def secondGet(rowIndex):
    curr = [1]
    temp = []
    for i in range(rowIndex):
        temp.append(curr[0])
        for j in range(1, len(curr)):
            temp.append(curr[j] + curr[j-1])
        temp.append(curr[-1])
        curr = temp
        temp = []
    return curr


first = timeit.Timer("firstGet(n)",
                     "from __main__ import firstGet, n")

second = timeit.Timer("secondGet(n)",
                      "from __main__ import secondGet, n")

# lets plot it
sample = 0
i_arr = []
f_arr = []
s_arr = []

# chart of data
print("Sample | Search | %-15s | %-15s" % ("First", "Second"))
print("--------------------------------------\n")
for i in range(0, 100, 10):
    n = i
    i_arr.append(i)
    f = first.timeit(number=1000)
    f_arr.append(f)
    s = second.timeit(number=1000)
    s_arr.append(s)
    sample += 1
    print("%-6s | %-6s | %-15.5f | %-15.5f" % (sample, i, f, s))

# plot of data
plt.scatter(i_arr, f_arr, color='red', label='First')
plt.scatter(i_arr, s_arr, color='blue', label='Second')
plt.grid()
plt.title('Time Complexity: First vs. Second Search')
plt.xlabel('Pascal Index')
plt.ylabel('Operation time in hundred-milliseconds')
plt.legend()
plt.show()
