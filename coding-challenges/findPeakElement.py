"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.
"""

class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        # defensive coding
        assert end >= start,"List cannot be empty"
        # if solutions are quick, avoid recursion
        if end == start:
            return 0
        elif end == start + 1:
            return start if nums[start] >= nums[end] else end
        else:
            return self.findPeakRecursively(nums, start, end, end)

    def findPeakRecursively(self, lst, s, e, n):
        m = int(s + (e-s)/2)
        if (m==0 or lst[m-1]<lst[m]) and (m==n or lst[m+1]<lst[m]):
            return m
        elif (m>0 and lst[m-1] > lst[m]):
            return self.findPeakRecursively(lst, s, m, n)
        else:
            return self.findPeakRecursively(lst, m+1, e, n)


nums = [1, 2, 3]

sol = Solution()

print(sol.findPeakElement(nums))
