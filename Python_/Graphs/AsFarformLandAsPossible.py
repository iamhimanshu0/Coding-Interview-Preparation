"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Input: grid = [[1,0,1],
               [0,0,0],
               [1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Input: grid = [[1,0,0],
               [0,0,0],
               [0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
"""
from re import L


grid = [[1,0,1],
        [0,0,0],
        [1,0,1]]

def maxDistance(grid):
    stack = []
    count  =0
    n = len(grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                count+=1
                stack.append((i,j,0))

    if not stack:
        return -1
    if count == n*n:
        return -1
    
    for i, j, d in stack:
        for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if 0<=x<n and 0<=y<n and grid[x][y]!=0:
                grid[x][y] =1
                stack.append((x,y,d+1))
    return stack[-1][-1]


# runtime :- O(m*n*n) , where m is the number of land cells.
# memory :- O(n*n) for the recursion
def maxDistanceDfs(grid):
    n = len(grid)
    dist = 0
    mx = 0

    def dfs(i,j, dist):
        if i <0 or i>= n or j <0 or j>= n or grid[i][j] !=0 and grid[i][j] <= dist:
            return

        grid[i][j] = dist
        dfs(i+1,j,dist+1)
        dfs(i-i,j,dist+1)
        dfs(i,j+1,dist+1)
        dfs(i,j-1, dist+1)
        

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                dfs(i,j,dist)

    for i in range(n):
        for j in range(n):
            if grid[i][j] >0:
                mx = max(mx, grid[i][j])
    
    return mx

print(
    # maxDistance(grid)
    maxDistanceDfs(grid)
) 


# https://leetcode.com/problems/as-far-from-land-as-possible/discuss/360963/C%2B%2B-with-picture-DFS-and-BFS