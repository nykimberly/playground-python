# -*- coding: utf-8 -*-


class Hourglass:

    def __init__(self, arr):
        self.arr = arr

    def sums(self):
        o = []
        o_rows = 4
        o_cols = 4
        for o_row in range(o_rows):
            ans = []
            for o_col in range(o_cols):
                currSum = \
                    sum(self.arr[o_row][o_col:o_col+3]) \
                    + self.arr[o_row+1][o_col+1] \
                    + sum(self.arr[o_row+2][o_col:o_col+3])
                ans.append(currSum)
            o.append(ans)
        return o

    def maxSum(self):
        o_rows = 4
        o_cols = 4
        maxSum = 0
        for o_row in range(o_rows):
            for o_col in range(o_cols):
                currSum = \
                    sum(self.arr[o_row][o_col:o_col+3]) \
                    + self.arr[o_row+1][o_col+1] \
                    + sum(self.arr[o_row+2][o_col:o_col+3])
                if currSum > maxSum:
                    maxSum = currSum
        return maxSum
