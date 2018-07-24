class Solution(object):
    def subsets(self, nums):
        return self.subsetutil(nums, [], [[]])

    def subsetutil(self, lst, d, res):
        if len(lst) <= 0:
            return
        self.subsetutil(lst[1:], [lst[0]] + d, res)
        self.subsetutil(lst[1:], d, res)
        res.append(d + [lst[0]])
        return res
