#Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid.


def isValid(s):

    sFreq = {char: 0 for char in s}

    minFreq = float("inf")
    real_sum = 0

    for char in s:
        sFreq[char] += 1

    for char in sFreq:
        if sFreq[char] < minFreq:
            minFreq = sFreq[char]
        real_sum += sFreq[char]

    proper_sum = len(sFreq) * minFreq

    if abs(real_sum - proper_sum) > 1:
        return "NO"
    else:
        return "YES"


print(isValid("abcdefghhgfedecba"))
