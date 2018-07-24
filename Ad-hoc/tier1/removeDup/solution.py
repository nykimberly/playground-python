class Solution(object):

    def removeDuplicates(self, nums):
        i = 1
        uniqueLength = len(nums)
        while i < uniqueLength:
            if nums[i] == nums[i-1]:
                nums.append(nums[i])
                del(nums[i])
                uniqueLength -= 1
            else:
                i += 1
        return uniqueLength
