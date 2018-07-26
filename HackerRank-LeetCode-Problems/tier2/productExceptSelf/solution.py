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