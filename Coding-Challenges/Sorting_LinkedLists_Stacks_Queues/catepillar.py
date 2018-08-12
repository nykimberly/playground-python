def leftover_leaves_1(num_leaves, caterpillar_jumps):
    eat_count = 0
    eaten = False
    # leftover_arr = list(i for i in range(1, num_leaves+1))
    for num_leaf in range(1, num_leaves+1):
        for num_jump in caterpillar_jumps:
            if num_leaf % num_jump == 0:
                eaten = True
        if eaten is True:
            eat_count += 1
            # leftover_arr.remove(num_leaf)
        eaten = False
    # print("I did not eat ", leftover_arr, len(leftover_arr))
    leftover = num_leaves - eat_count
    return leftover


def leftover_leaves_2(num_leaves, jumps):

    subsets = []
    n = len(jumps) - 1
    sub_pairs(jumps, 0, n, [], subsets)

    eaten = 0
    for num_jump in jumps:
        eaten += num_leaves//num_jump

    for subset in subsets:
        composite_lcm = find_lcm(subset[0], subset[1])
        for i in range(2, len(subset)):
            composite_lcm = find_lcm(composite_lcm, subset[i])
        if len(subset) % 2 == 0:
            eaten -= num_leaves//composite_lcm
        else:
            eaten += num_leaves//composite_lcm

    leftover = num_leaves - eaten
    return leftover


def sub_pairs(arr, s, e, sub_arr, subsets):
    if s == e + 1:
        if len(sub_arr) > 1 and len(sub_arr) <= len(arr):
            subsets.append(sub_arr)
        return subsets
    sub_pairs(arr, s+1, e, sub_arr, subsets)
    sub_pairs(arr, s+1, e, sub_arr+[arr[s]], subsets)


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


print(leftover_leaves_1(10, [2, 3, 5]))
print(leftover_leaves_2(10, [2, 3, 5]))