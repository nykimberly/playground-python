class Solution(object):

    def pivotIndex(self, nums):
        sumL = 0
        sumR = sum(nums[1:])
        for p in range(len(nums)):
            if sumL == sumR:
                return p
            else:
                sumL += nums[p]
                if p == len(nums) - 1:
                    sumR = 0
                else:
                    sumR -= nums[p+1]
        return -1


"""
    def pivotIndex(self, nums):
        # initialize sumL and sumR s.t. first comparison
        # captures case where pivot val is 0
        sumL = 0
        sumR = sum(nums[1:])

        # capture case where 0 <= piv < len(nums)
        for p in range(len(nums) - 1):
            if sumL == sumR:
                return p
            sumL += nums[p]
            sumR -= nums[p+1]

        # now capture case where pivot val is len(nums)
        if sum(nums[:-1]) == 0:
            return len(nums)
        return -1
"""
