"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        runningMin = float("inf")
        currentMax = 0
        for price in prices:
            if price < runningMin:
                runningMin = price
            if price - runningMin > currentMax:
                currentMax = price - runningMin
        return currentMax