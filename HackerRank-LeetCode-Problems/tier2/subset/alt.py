class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetutil(nums, [], [[]])

    def subsetutil(self, lst, d, res):
        if len(lst) <= 0:
            return
        self.subsetutil(lst[1:], d + [lst[0]], res)
        self.subsetutil(lst[1:], d, res)
        res.append(d + [lst[0]])
        return res
