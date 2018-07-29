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
