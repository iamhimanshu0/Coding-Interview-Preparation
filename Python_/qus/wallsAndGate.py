"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a Gate, that room should remain filled with INF

Input:
    [[2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]

Output:
    [[3,-1,0,1],
     [2,2,1,-1],
     [1,-1,2,-1],
     [0,-1,3,4]]

Explanation:
the 2D grid is:

    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
    0  -1 INF INF

the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

from collections import deque


grid  = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]

def wallGates(grid):
    row, col = len(grid), len(grid[0])
    queue = deque()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 0:
                queue.append((r,c))

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            new_x = dx+x
            new_y = dy+y

            if new_x < 0 or new_x >= row or new_y <0 or new_y >= col or grid[new_x][new_y] < grid[x][y]+1:
                continue
            
            grid[new_x][new_y] = grid[x][y] +1
            queue.append((new_x, new_y))

    return grid


print(
    wallGates(grid)
)