class Solution(object):
    def searchInsert(self, nums, target):
        for i, n in enumerate(nums):
            if n == target:
                return i
            if n > target:
                nums.insert(i, target)
                return i
        return len(nums)
