from collections import Counter

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    multiplier = n // len(s)
    s_count = Counter(s).get("a", 0)
    remainder = n % len(s)
    r_count = Counter(s[:remainder]).get("a", 0)
    return multiplier * s_count + r_count

if __name__ == '__main__':
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)