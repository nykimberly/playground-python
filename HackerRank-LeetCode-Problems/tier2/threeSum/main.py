# -*- coding: utf-8 -*-

from solution import Solution

arr = [1, 2, -2, -1]
# 0 - (-1 + 0) = 1: 0, 1
# 0 - (-1 + 1) = 0:, 0, 2
# 0 - (0 + 1) = -1: 1, 2
# soln = -1, 0, 1
# soln = 1, -2, 1

sol = Solution()
print(sol.threeSum(arr))

lst = [-1,0,1,2,-1,-4]

print(sol.threeSum(lst))
