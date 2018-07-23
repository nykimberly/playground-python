class Solution(object):

    # O(log(2, n) time)
    def findPeakElement(self, nums):
        # get some list properties to see if we can quickly solve w/o recursion
        n = len(nums)
        s = 0
        e = n - 1
        # case where list is empty
        assert e >= s, "List cannot be empty"
        # case where list is one element
        if e == s:
            return 0
        # case where list is two elements
        elif e == s + 1:
            return s if nums[s] >= nums[e] else e
        # if list has more than two elements then we can recurse
        else:
            return self.findPeakHelper(nums, s, e, n)

    def findPeakHelper(self, l, s, e, n):
        # calculate mid index
        m = int(s + (e-s) / 2)
        # base cases where m=0 or or n-1 is accounted for in the if statements
        # solution must exist since we consider values outside l to be -inf
        # case where m is peak
        if ((m == 0 or l[m-1] < l[m]) and (m == n-1 or l[m+1] < l[m])):
            print("first case")
            return m
        # case where peak is to the left or m is at right boundary
        elif (m > 0 and l[m-1] > l[m]):
            print("second case")
            return self.findPeakHelper(l, s, m, n)
        # case where peak is to the right or m is at left boundary
        elif (m < n-1 and l[m+1] > l[m]):
            print("third case")
            return self.findPeakHelper(l, m+1, e, n)
        else:
            return "Didn't account for this case"
