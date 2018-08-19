"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        soln = []
        for i in range(numRows):
            row = [1]
            if i > 0:
                if i > 1:
                    for j in range(1, i):
                        row.append(soln[i-1][j-1] + soln[i-1][j])
                row.append(1)
            soln.append(row)
        return soln


sol = Solution()

print(sol.generate(0))
print(sol.generate(1))
print(sol.generate(2))
print(sol.generate(3))
print(sol.generate(4))
print(sol.generate(5))
