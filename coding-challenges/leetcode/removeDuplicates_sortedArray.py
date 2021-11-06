"""
Remove duplicates from sorted array
"""

class Solution(object):

    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del(nums[i])
            else:
                i += 1
        return len(nums)


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

sol = Solution()
print(sol.removeDuplicates(arr))
