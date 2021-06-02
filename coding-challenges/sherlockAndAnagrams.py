import math

from collections import Counter, defaultdict

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    substring_counts = defaultdict(int)
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            substring_counts[tuple(sorted(substr))] += 1
    return int(
        sum(
            math.factorial(count) / (math.factorial(count-2)*math.factorial(2))
            for count in substring_counts.values() if count > 1
        )
    )


if __name__ == '__main__':
    s = input()
    result = sherlockAndAnagrams(s)
    print(result)