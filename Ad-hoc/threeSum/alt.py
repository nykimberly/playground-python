class Solution(object):
    def threeSum(self, nums):
        solns = set()
        pairSums = dict()
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                comp = 0 - nums[j]
                if comp in pairSums:
                    if j not in pairSums[comp]:
                        val1 = nums[pairSums[comp][0]]
                        val2 = nums[pairSums[comp][1]]
                        val3 = nums[j]
                        triplet = sorted([val1, val2, val3])
                        solns.add(tuple(triplet))
                s = nums[i] + nums[j]
                pairSums[s] = [i, j]
        solns = list(solns)
        for i in range(len(solns)):
            solns[i] = list(solns[i])
        return solns