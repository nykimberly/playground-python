import timeit
import matplotlib.pyplot as plt


def leftover_leaves_1(num_leaves, caterpillar_jumps):
    eat_count = 0
    eaten = False
    # leftover_arr = list(i for i in range(1, num_leaves+1))
    for num_leaf in range(1, num_leaves+1):
        for num_jump in caterpillar_jumps:
            if num_leaf % num_jump == 0:
                eaten = True
                break
        if eaten is True:
            eat_count += 1
            # leftover_arr.remove(num_leaf)
        eaten = False
    # print("I did not eat ", leftover_arr, len(leftover_arr))
    leftover = num_leaves - eat_count
    return leftover


def leftover_leaves_2(num_leaves, jumps):

    pairs = []
    n = len(jumps) - 1
    sub_pairs(jumps, 0, n, [], pairs)

    eaten = 0
    for num_jump in jumps:
        eaten += num_leaves//num_jump

    for pair in pairs:
        composite_lcm = find_lcm(pair[0], pair[1])
        for i in range(2, len(pair)):
            composite_lcm = find_lcm(composite_lcm, pair[i])
        if len(pair) % 2 == 0:
            eaten -= num_leaves//composite_lcm
        else:
            eaten += num_leaves//composite_lcm

    leftover = num_leaves - eaten
    return leftover


def sub_pairs(arr, s, e, sub_arr, pairs):
    if s == e + 1:
        if len(sub_arr) > 1 and len(sub_arr) <= len(arr):
            pairs.append(sub_arr)
        return pairs
    sub_pairs(arr, s+1, e, sub_arr, pairs)
    sub_pairs(arr, s+1, e, sub_arr+[arr[s]], pairs)


def find_lcm(num1, num2):
    if(num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

# def timeit_plot(m1_name, methodt1, m2_name, methodt2, n_name, N, k_name, K):


m1_name = "2Loops"
method_test_1 = timeit.Timer(
        "leftover_leaves_1(n, k[:i])",
        "from __main__ import leftover_leaves_1, n, k, i")
m2_name = "Math"
method_test_2 = timeit.Timer(
        "leftover_leaves_2(n, k[:i])",
        "from __main__ import leftover_leaves_2, n, k, i")
n_name = "Leaves"
n = 100
k_name = "# Caterpillars"
k = list(x for x in range(2, 8, 1))
k_length = len(k)

sample = 0
i = 1
k_x = []
method1_y = []
method2_y = []
print("%-6s | %-6s | %-37s | %-6s | %7s | %-6s | %7s"
      % ("Sample", n_name, k_name,
         m1_name, "leftover", m2_name, "leftover"))
while i <= k_length:
    k_x.append(i)
    m1 = method_test_1.timeit(number=1000)
    l1 = leftover_leaves_1(n, k[:i])
    method1_y.append(m1)
    m2 = method_test_2.timeit(number=1000)
    l2 = leftover_leaves_2(n, k[:i])
    method2_y.append(m2)
    print("%-6s | %-6s | %-37s | %-6.3f | %8d | %-6.3f | %7d"
          % (sample, n, k[:i], m1, l1, m2, l2))
    i += 1
    sample += 1

plt.scatter(k_x, method1_y, color='red', label=str(m1_name))
plt.scatter(k_x, method2_y, color='blue', label=str(m2_name))
plt.grid()
plt.title("Time Complexity: " +
          str(m1_name) + " vs " + str(m2_name))
plt.xlabel(k_name)
plt.ylabel('Operation time in milliseconds')
plt.legend()
plt.show()
