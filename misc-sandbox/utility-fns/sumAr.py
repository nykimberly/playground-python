# -*- coding: utf-8 -*-

def sum(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum

# wrong type
sum("12")
sum("okay")
sum(["okay"])

# noniterable argument
sum(0)

# too many arguments
sum(1, 2)

# proper input
sum([]) == 0
sum([1]) == 1
sum([1, 3, 4, 0, 11]) == 1 + 3 + 4 + 0 + 11
sum([1.1, 3, -4, 0, 11]) == 11.1