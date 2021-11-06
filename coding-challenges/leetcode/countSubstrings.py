# Given a string, your task is to count how many palindromic substrings in this string. The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.


class Solution:
    def countSubstrings(self, s):
        N = len(s)
        result = 0
        for i in range(2*N-1):
            left = i//2
            right = (i+1)//2
            while left >= 0 and right < N and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        return result


sol = Solution()
sol.countSubstrings("aabc")
