import math
import os
import random
import re
import sys

# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

def sockMerchant(n, ar):
    socks_by_color = {}
    for sock in ar:
        if sock in socks_by_color:
            socks_by_color[sock] += 1
        else:
            socks_by_color[sock] = 1
    return int(sum(math.floor(sock_count / 2) for sock_count in socks_by_color.values()))
    
if __name__ == '__main__':
    n = int(raw_input().strip())
    ar = map(int, raw_input().rstrip().split())
    result = sockMerchant(n, ar)
    print(result)
