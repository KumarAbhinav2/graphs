"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""


class Solution:
    def numIslands(self, grid) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # root node for dfs
                if grid[i][j] == '1':
                    islands += 1
                    # expand to find all the land
                    self.dfs(grid, i, j)
        return islands

    def dfs(self, grid, r, c):
        grid[r][c] = "0"
        # find all the possible adjacent nodes to see its a valid island
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                self.dfs(grid, nr, nc)