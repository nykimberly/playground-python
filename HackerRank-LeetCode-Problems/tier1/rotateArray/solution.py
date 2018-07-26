"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution(object):
    # O(n) space solution
    """
    def rotate(self, nums, k):
        temp = list(nums)
        length = len(nums)
        for i, e in enumerate(temp):
            n = (i + k) % length
            nums[n] = e
    """
    # O(c) space solution
    """
    def rotate(self, nums, k):
        og_last = len(nums) - 1
        nums.append(nums[og_last])
        for r in range(k):
            for i in range(og_last + 1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = nums[og_last + 1]
        nums.pop()
    """
    # O(1) space solution
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        end = len(nums)
        k = k % end
        nums[:] = nums[end-k:] + nums[:end-k]
        
