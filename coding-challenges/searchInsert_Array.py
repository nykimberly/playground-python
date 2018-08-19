# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n >= target:
                return i
        return len(nums)


arr = [1, 3, 5, 7, 8]
tar = 7
sol = Solution()
print(sol.searchInsert(arr, tar))
