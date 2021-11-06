#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. Note: The solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums):
        nums.sort()
        target = 0
        solns = []
        for i in range(len(nums)):
            comp = target-nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                pair = nums[start] + nums[end]
                if pair < comp:
                    start += 1
                elif pair > comp:
                    end -= 1
                else:
                    solns.append((nums[end], nums[i], nums[start]))
                    start += 1
                    end -= 1
        solns = set(solns)
        solns = list(solns)
        for i in range(len(solns)):
            solns[i] = list(solns[i])
        return solns


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
