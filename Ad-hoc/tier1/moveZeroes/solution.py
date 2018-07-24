class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # initialize pointer
        i = 0
        # initialize variable 'end' of nonzero list
        end = len(nums)
        # while i is less than this end
        while i < end:
            # check if nums at i is zero
            if nums[i] == 0:
                # if it is, then concatenate zero to end of rest of list
                nums[i:] = nums[i+1:] + [nums[i]]
                # decrement end
                end -= 1
            else:
                # if num at i is not zero, move to next val
                i += 1
