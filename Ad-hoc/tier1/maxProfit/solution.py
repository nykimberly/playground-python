class Solution(object):

    def maxProfit(self, prices):
        runningMin = float("inf")
        maxProfit = 0
        for day, price in enumerate(prices):
            if price < runningMin:
                runningMin = price
            if price - runningMin > maxProfit:
                maxProfit = price - runningMin
        return maxProfit

    # runtime too high
    """
    def maxProfit(self, prices):
        maxProfit = 0
        days = len(prices)
        for buyday in range(days):
            for sellday in range(buyday + 1, days):
                if prices[sellday] - prices[buyday] > maxProfit:
                    maxProfit = prices[sellday] - prices[buyday]
        return maxProfit
    """
