import timeit
import matplotlib.pyplot as plt

# instantiate Timer objects in main space
# timeit module will capture time
popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")

popend = timeit.Timer("y.pop()",
                      "from __main__ import y")

# start off with lists of 2 million elements
x = list(range(2000000))
y = list(range(2000000))

# compare performance of 1000 pop operations
popzero_t = popzero.timeit(number=1000)
print("popzero performance time at list size = 2e6: %.5f " % popzero_t)
popend_t = popend.timeit(number=1000)
print("popend performance time at list size = 2e6: %.5f " % popend_t)

# lets plot it
sample = 0
i_arr = []
pe_arr = []
pz_arr = []

# chart of data
print("Sample | %-15s | %-15s" % ("pop()", "pop(0)"))
print("--------------------------------------\n")
# increment from 100,000 to 3mil in steps of 10,000
for i in range(100000, 3000001, 10000):
    i_arr.append(i)
    x = list(range(i))
    pe = popend.timeit(number=1000)
    pe_arr.append(pe)
    y = list(range(i))
    pz = popzero.timeit(number=1000)
    pz_arr.append(pz)
    sample += 1
    print("%-6s | %-15.5f | %-15.5f" % (sample, pe, pz))

# plot of data
plt.scatter(i_arr, pe_arr, color='blue', label='Pop()')
plt.scatter(i_arr, pz_arr, color='red', label='Pop(0)')
plt.grid()
plt.title('Time Complexity: Pop() vs Pop(0)')
plt.xlabel('List size')
plt.ylabel('Operation time in milliseconds')
plt.legend()
plt.show()
