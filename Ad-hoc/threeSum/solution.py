class Solution(object):
    def threeSum(self, nums):
        # sort list, log(n) operation
        lst = sorted(nums)
        # initialize set, used to return unique solns only
        solns = set()
        # loop through sorted list
        for i in range(len(lst)):
            # grab the complement of current val
            comp = -lst[i]
            # iterate through rest of list, starting from i
            j = i + 1
            end = len(lst) - 1
            while j < end:
                # grab sum
                s = lst[j] + lst[end]
                # if sum is less than complement, increment lower val forward
                if s < comp:
                    j += 1
                # if sum is greater than complement, increment higher val back
                elif s > comp:
                    end -= 1
                else:
                    solns.add((lst[end], lst[i], lst[j]))
                    j += 1
                    end -= 1
        solns = list(solns)
        for i in range(len(solns)):
            solns[i] = list(solns[i])
        return solns
