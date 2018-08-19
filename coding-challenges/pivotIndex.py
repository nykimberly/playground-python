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


nums = []

sol = Solution()

print(sol.pivotIndex(nums))
