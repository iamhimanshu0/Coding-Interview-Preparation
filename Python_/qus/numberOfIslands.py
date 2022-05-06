"""
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
    if not grid: return 0
    row, column = len(grid), len(grid[0])
    islands = 0

    def dfs(i,j):
        if i <0 or i >=row or j<0 or j>= column or grid[i][j] != "1":
            return 
        grid[i][j] = "#"
        dfs(i+1,j), dfs(i-1,j), dfs(i,j+1), dfs(i,j-1)

    for i in range(row):
        for j in range(column):
            if grid[i][j] == "1":
                dfs(i,j)
                islands +=1
    return islands

print(
    numIslands(grid)
)