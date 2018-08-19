"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = list(1 for i in range(n))
        print(output)
        prod_forward = 1
        # accumulate products forward
        for i in range(n-1):
            prod_forward *= nums[i]
            output[i+1] = prod_forward
        print(output)
        prod_backward = 1
        # accumulate products backwards
        for i in range(n-1, 0, -1):
            prod_backward *= nums[i]
            output[i-1] *= prod_backward
        print(output)
        return output


arr = [1, 2, 3, 4]
# 0 - (-1 + 0) = 1: 0, 1
# 0 - (-1 + 1) = 0:, 0, 2
# 0 - (0 + 1) = -1: 1, 2
# soln = -1, 0, 1
# soln = 1, -2, 1

sol = Solution()
print(sol.productExceptSelf(arr))
