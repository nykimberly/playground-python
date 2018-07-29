class Solution(object):
    def romanToInt(self, s):
        romanConversion = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        i = 0
        sum = 0
        l = list(romanConversion[char] for char in s)
        n = len(l) - 1
        while i <= n:
            if i < n and l[i] < l[i+1]:
                l[i] = l[i+1] - l[i]
                del(l[i+1])
                n -= 1
            sum += l[i]
            i += 1
        return sum
