class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        N = len(s)
        result = 0

        # there are 2n-1 comparisons to be made
        for i in range(2*N-1):
            # by floor/integer dividing left and right,
            # we hold one constant while incrementing to the other, alternating
            left = i//2
            right = (i+1)//2
            # basically, we check equality between s[left] and s[right]
            while left >= 0 and right < N and s[left] == s[right]:
                # every equality means another palindrome
                result += 1
                left -= 1
                right += 1
        return result
