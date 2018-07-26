def isValid(s):

    sFreq = { char: 0 for char in s }
    
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

"""
aa
bb
cc
dd
ff
gg
hh
eee
"""