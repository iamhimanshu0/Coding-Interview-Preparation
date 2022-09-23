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
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def numIslands(grid):
    if not grid:
        return 0
    ROWS, COLS = len(grid), len(grid[0])
    maxCount = 0

    def dfs(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
            return
        grid[r][c] = "#"
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "1":
                dfs(i, j)
                maxCount += 1

    return maxCount


print(
    numIslands(grid)
)
