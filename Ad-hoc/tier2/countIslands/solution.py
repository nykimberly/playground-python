class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] != grid[i+1][j]
                    grid[i][j] != grid[i-1][j]
                    grid[i][j] != grid[i][j+1]
                    grid[i][j] != grid[i][j-1]