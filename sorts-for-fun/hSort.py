# -*- coding: utf-8 -*-

class Solution:

    def heapSort(self, nums, k):

        end = len(nums)

        for i in range(end, -1, -1):
            self.heapify(nums, i, end)

        for n in range(end-1, -1, -1):
            print(nums)
            nums[0], nums[n] = nums[n], nums[0]
            # quick hack to reverse list
            # nums.append(nums[n])
            # del(nums[n])
            self.heapify(nums, 0, n)
        print(nums)

    def heapify(self, arr, root, end):

        largest = root
        left = 2*root + 1
        right = 2*root + 2

        if left < end and arr[largest] < arr[left]:
            largest = left

        if right < end and arr[largest] < arr[right]:
            largest = right

        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            self.heapify(arr, largest, end)

nums = [1, 12, 11, 13, 5, 6, 7]
k = 7

sol = Solution()

sol.heapSort(nums, 7)