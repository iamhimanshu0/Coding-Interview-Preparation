"""
# https://leetcode.com/problems/number-of-enclaves/

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Input: grid = [[0,0,0,0],
               [1,0,1,0],
               [0,1,1,0],
               [0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Input: grid = [[0,1,1,0],
               [0,0,1,0],
               [0,0,1,0],
               [0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
"""

grid =[[0,0,0,1,1,1,0,1,0,0],
       [1,1,0,0,0,1,0,1,1,1],
       [0,0,0,1,1,1,0,1,0,0],
       [0,1,1,0,0,0,1,0,1,0],
       [0,1,1,1,1,1,0,0,1,0],
       [0,0,1,0,1,1,1,1,0,1],
       [0,1,1,0,0,0,1,1,1,1],
       [0,0,1,0,0,1,0,1,0,1],
       [1,0,1,0,1,1,0,0,0,0],
       [0,0,0,0,1,1,0,0,0,1]]

"""
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], 
 [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], 
 [0, 0, 1, 0, 1, 1, 1, 1, 0, 0], 
 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 1, 0, 0, 1, 0, 0, 0, 0], 
 [0, 0, 1, 0, 1, 1, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""

"""
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""

def numEnclaves(grid):
    r,c = len(grid), len(grid[0])
    enclaves = 0

    def dfs(i,j):
        if i <0 or i >= r or j< 0 or j >= c or grid[i][j] == 0:
            return        
        grid[i][j] = 0 
        dfs(i+1,j)
        dfs(i-i,j)
        dfs(i,j+1)
        dfs(i,j-1)

    for i in range(r):
        for j in range(c):
            # making all the ones which are connected with the boundry element
            if grid[i][j] == 1 or (i ==0 or j==0 or i ==r-1 or j == c-1):
                dfs(i,j)                
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                enclaves +=1
    print(grid)
    return enclaves


def test(A):
    def dfs(i, j):
        A[i][j] = 0
        for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if 0 <= x < m and 0 <= y < n and A[x][y]:
                dfs(x, y)
    m, n = len(A), len(A[0])
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1 or (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                dfs(i, j)

    print(A)
    return sum(sum(row) for row in A)


print(
    numEnclaves(grid)
)