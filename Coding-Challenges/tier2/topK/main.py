from solution import Solution

nums = [-1, 2, -1, 2, 3, 2, 5,  3, 7, 8, 9, 10]
print(sorted(nums))
k = 10

sol = Solution()

print(sol.topKFrequent(nums, k))
