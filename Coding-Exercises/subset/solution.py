class Solution(object):
    def subsets(self, nums):
        res = []
        return self.subsetutil(nums, 0, len(nums)-1, [], res)

    def subsetutil(self, arr, start, end, sub_arr, ss):
        if start == end + 1:
            ss.append(sub_arr)
            print(ss)
            return ss
        self.subsetutil(arr, start+1, end, sub_arr, ss)
        self.subsetutil(arr, start+1, end, sub_arr+[arr[start]], ss)
