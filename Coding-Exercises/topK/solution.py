class Solution:

    def topKFrequent(self, nums, k):

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        top = [key for key in freq]

        end = len(top)
        for i in range(end, -1, -1):
            self.heapify(top, freq, i, end)

        for n in range(end-1, -1, -1):
            top[0], top[n] = top[n], top[0]
            self.heapify(top, freq, 0, n)

        return top[:k]

    def heapify(self, arr, freq, root, end):

        smallest = root
        left = 2*root + 1
        right = 2*root + 2

        if left < end and freq[arr[left]] < freq[arr[smallest]]:
            smallest = left

        if right < end and freq[arr[right]] < freq[arr[smallest]]:
            smallest = right

        if smallest != root:
            arr[smallest], arr[root] = arr[root], arr[smallest]
            self.heapify(arr, freq, smallest, end)
