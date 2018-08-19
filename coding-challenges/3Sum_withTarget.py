class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        # print(nums)
        closest = float("inf")
        for i in range(len(nums)):
            start, end = i + 1, len(nums)-1
            while start < end:
                # print(i, start, end)
                triplet = nums[i] + nums[start] + nums[end]
                # print("triplet is ", triplet)
                # print("closest", closest)
                if triplet < target:
                    if abs(target-triplet) < abs(target-closest):
                        closest = triplet
                        # print("assigned", closest)
                    start += 1
                elif triplet > target:
                    if abs(target-triplet) < abs(target-closest):
                        closest = triplet
                        # print("assigned", closest)
                    end -= 1
                else:
                    closest = triplet
                    return closest
        # print("answer is")
        return closest


arr = [0, 1, 2]
target = 3
sol = Solution()
print(sol.threeSumClosest(arr, target))
