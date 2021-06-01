import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    num_valleys = 0
    altitude = 0
    for step in path:
        if step == "U":
            altitude += 1
        if step == "D":
            altitude -= 1
        if altitude == 0 and step == "U":
            num_valleys += 1
    return num_valleys


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)

