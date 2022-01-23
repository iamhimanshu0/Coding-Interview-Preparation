"""
# https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numIslands(grid):
    ROW, COLS = len(grid), len(grid[0])


    def dfs(i,j):
        if i < 0 or i >= ROW or j < 0 or j >= COLS or grid[i][j] != "1":
            return 
        grid[i][j] = "#"
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    island = 0

    for i in range(ROW):
        for j in range(COLS):
            if grid[i][j] == "1":
                dfs(i,j)
                island += 1
    


    return island


print(
    numIslands(grid)
)
