# -*- coding: utf-8 -*-

from solution import Interval, Solution
arr = [
    Interval(0, 1),
    Interval(5, 10),
    Interval(1, 3),
    Interval(0, 7),
    Interval(11, 14)]

sol = Solution()
i = sol.merge(arr)

for interval in arr:
    print(interval.start, interval.end)

print("===============")
for interval in i:
    print(interval.start, interval.end)
