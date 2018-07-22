class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # pointer for first list
        i = 0
        # pointer for second ist
        j = 0
        # end value of merged list
        end = m

        while (i < end) & (j < n):
            # if element in second list is less than element in first list
            if nums2[j] < nums1[i]:
                # move rest of first list forward one
                nums1[i+1:end+1] = nums1[i:end]
                # and assign index to element of second list
                nums1[i] = nums2[j]
                # increment second list pointer
                j += 1
                # increment end value of merged list
                end += 1
            # otherwise
            else:
                # increment first list pointer
                i += 1

        # if only list2 elements are left, copy rest of list2 elements over
        if (j < n):
            nums1[i:] = nums2[j:]
            end += (n-j)

        # situation where only list 1 elements are left
        # just return since elements are already on first list
        return
