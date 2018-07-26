# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, i):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        count = 0
        ordered = []
        minStart = float("inf")
        while count < len(i):
            if i[count].start < minStart:
                minStart = i[count].start
                ordered.insert(0, i[count])
            else:
                
            count += 1
        return ordered