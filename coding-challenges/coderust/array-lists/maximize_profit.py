"""
Given a list of daily stock prices (integers for simplicity), return the buy and sell prices for making the maximum profit/minimize loss
"""

def optimal_buy_sell(l):
    """
    There are n buy scenarios, where optimal sell day is the
    max value of the remaining subarray (from buy point to end)

    So we'll want to go through and find the max sell day (idx)
    for each buy scenario by getting the max of the remaining
    subarray and storing that i.e.

    l = [10, 9, 2, 7]

    max_idx_remaining = [
        0, 1, 3, 3
    ]
    where
        max l[3:] is l[3]
        max l[2:] is l[3]
        max l[1:] is l[1]
        max l[0:] is l[0]

    then it's simply a matter of computing the optimal scenario

    l[max_idx_remaining[1]] - l[0] = 9 - 10 = -1
    l[max_idx_remaining[2]] - l[1] = 7 - 9 = -2
    l[max_idx_remaining[3]] - l[2] = 7 - 2 = 5

    therefore optimal solution is buy at 2 and sell at 7
    """
    max_idx_remaining = []
    curr_max = (None, None)
    for i in range(len(l) - 1, -1, -1):
        if not curr_max[-1] or l[i] > curr_max[-1]:
            curr_max = (i, l[i])
        max_idx_remaining.insert(0, curr_max[0])

    buy_sell_max = (None, None, None)
    for i in range(len(l) - 2):
        buy_price = l[i]
        sell_price = l[max_idx_remaining[i+1]]
        difference = sell_price - buy_price
        if not buy_sell_max[-1] or difference > buy_sell_max[-1]:
            buy_sell_max = (buy_price, sell_price, difference)
    return buy_sell_max[:2]


if __name__ == "__main__":
    i = [8, 5, 12, 9, 19, 1]
    o = optimal_buy_sell(i)
    e = (5, 19)
    assert o == e, f"Expected {e}, got {o}"

    i = [21, 12, 11, 9, 6, 3]
    o = optimal_buy_sell(i)
    e = (12, 11)
    assert o == e, f"Expected {e}, got {o}"

    print("Success!")