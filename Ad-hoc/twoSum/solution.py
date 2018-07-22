class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair = []
        for i, e in enumerate(numbers):
            if e in pair:
                return [pair.index(e) + 1, i + 1]
            pair.append(target - e)
