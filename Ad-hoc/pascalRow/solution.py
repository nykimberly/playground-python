class Solution(object):
    def getRow(rowIndex):
        soln = [1]
        for i in range(1, rowIndex + 1):
            output = [1]
            for j in range(1, i + 1):
                if (j == i):
                    val = 1
                else:
                    val = soln[i-1][j-1] + soln[i-1][j]
                output.append(val)
            soln.append(output)
        return soln[rowIndex]
