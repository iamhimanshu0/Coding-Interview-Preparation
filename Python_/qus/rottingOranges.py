"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from collections import deque


grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

def orangesRotting(grid):
    if not grid: return -1
    row, col = len(grid), len(grid[0])

    # keep track the fresh orange
    fresh_count = 0 
    
    # queue with rotten oranges (BFS)
    rotten = deque()

    # visit each cell in the grid
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 2:
                rotten.append((r,c))
            elif grid[r][c] == 1:
                fresh_count +=1
    
    # keep track the min passed
    minutes_passed = 0

    while rotten and fresh_count > 0:

        minutes_passed +=1

        for _ in range(len(rotten)):
            x,y = rotten.popleft()

            # visit all the adjecent cells
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                # get new coordinates
                xx, yy = x+dx , y+dy
                
                # ignore if cell is out of the grid boundary
                if xx < 0 or xx == row or yy < 0 or yy == col:
                    continue
                
                # ignore the cells for '0' and '2'
                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue
                    
                # update fresh orange
                fresh_count -=1

                # make orange rotten
                grid[xx][yy] = 2

                # append current rotten to the queue
                rotten.append((xx,yy))

    return minutes_passed if fresh_count == 0 else -1

print(orangesRotting(grid))