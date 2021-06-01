import math
import os
import random
import re
import sys

from collections import Counter

# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

def sockMerchant(ar):
    socks_by_color = Counter(ar)
    return sum(sock_count // 2 for sock_count in socks_by_color.values())


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

