"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Input: grid = [[0,0,1,0,0],
               [0,1,0,1,0],
               [0,1,1,1,0]]
Output: 1

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
"""

grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]

def closedIsland(grid):
    if not grid or not grid[0]:
            return 0
        
    m, n = len(grid), len(grid[0])
    
    def dfs(i, j, val):
        if 0<=i<m and 0<=j<n and grid[i][j]==0:
            grid[i][j] = val
            dfs(i, j+1, val)
            dfs(i+1, j, val)
            dfs(i-1, j, val)
            dfs(i, j-1, val)
    
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                dfs(i, j, 1)
            
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                dfs(i, j, 1)
                res += 1
                
    return res


print(
    closedIsland(grid)
)