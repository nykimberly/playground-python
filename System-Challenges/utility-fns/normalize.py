# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv("Test_Data.csv")
salary_col = data.iloc[:, 3].values
arr = [1, -2, 0, 3]
ans = [-50, -25, 0, 25, 50]
# -50 -25    0   +25  +50
#  0  0.25  0.5  0.75  1

def normalize(col):

    # calculate spread
    minVal = 0
    maxVal = 0
    for item in col:
        if item < minVal:
            minVal = item
        if item > maxVal:
            maxVal = item

    # normalize results in arr
    addVal = 0
    if minVal < 0:
        addVal = 0 - minVal
    spread = maxVal - minVal
    results = []
    for item in col:
        res = (item + addVal)/spread
        assert res >= 0, str(res) + "need higher addVal to convert to positive"
        assert res <= 1, str(res) + "result is not less than one"
        results.append(res)

    return results

print(normalize(ans))
print(normalize(ans) == [0, 0.25, 0.5, 0.75, 1])