# -*- coding: utf-8 -*-

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        print(grid)
        self.travel(grid, 0, 0, "water", 0)

    def travel(self, grid, x, y, status, count):
        if x >= len(grid[0]) or y >= len(grid):
            return count
        print("current count is", count)
        print(grid[y][x])
        if grid[y][x] == "1":
            if status != "land":
                count += 1
            status = "land"
        else:
            if status != "water":
                count += 1
            status = "water"
            print("we are on water!")
        self.travel(grid, x+1, y, status, count)
        self.travel(grid, x, y+1, status, count)
