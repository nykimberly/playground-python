"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        curr = 0
        nonzero_end = len(nums)
        while curr < nonzero_end:
            if nums[curr] == 0:
                nums[curr:] = nums[curr+1:] + [nums[curr]]
                nonzero_end -= 1
            else:
                curr += 1


nums = [0, 0, 0, 1, 0, 2, 0]

sol = Solution()
print(sol.moveZeroes(nums))

