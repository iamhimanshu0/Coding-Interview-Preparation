"""
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Input: grid = [[0,1],[1,0]]
Output: 2

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""

from collections import deque


grid = [[0,1],[1,0]]

def shortestPathBinaryMatrix(grid):
    # if not grid: return -1
    # if grid[0][0] == "1": return -1
     
    ROW, COL = len(grid), len(grid[0])
    visited = set()
    q = deque()
    dirs = [(0,1),(0,-1),(1,0),(-1,0),
            (-1,-1), (-1,1),(1,-1),(1,1)]

    if grid[0][0] == 0:
        q.append((1,(0,0)))
        visited.add((0,0))

    print(q)
    while q:
        steps, tmp = q.popleft()
        r,c = tmp[0],tmp[1]

        if (r,c) == (ROW-1, COL-1):
            return steps
        
        for i, j in dirs:
            new_r, new_c = r+i, c+j 
            if 0 <= new_r < ROW and 0 <= new_c  < COL and grid[new_r][new_c]==0 and (new_r, new_c) not in visited:
                q.append((steps+1,(new_r, new_c)))
                visited.add((new_r, new_c))

    return -1 


print(
    shortestPathBinaryMatrix(grid)
)