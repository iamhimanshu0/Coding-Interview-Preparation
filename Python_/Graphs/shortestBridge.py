"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Input: grid = [[0,1],
               [1,0]]
Output: 1

Input: grid = [[0,1,0],
               [0,0,0],
               [0,0,1]]
Output: 2

Input: grid = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,1,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]]
Output: 1
"""

import collections

grid = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

def shortestBridge(grid):
    m,n = len(grid), len(grid[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    seen = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue = collections.deque([(i,j)])
                seen.add((i,j))
                # traverse first island
                while queue:
                    cur_i, cur_j  =queue.popleft()

                    for d in directions:
                        new_i = cur_i + d[0]
                        new_j = cur_j + d[1]

                        if 0<=new_i<m and 0<=new_j<n and grid[new_i][new_j]==1 and (new_i, new_j) not in seen:
                            queue.append((new_i, new_j))
                            seen.add((new_i, new_j))

                # expand the first island:
                queue = collections.deque(seen)
                distance =0

                while queue:
                    for _ in range(len(queue)):
                        cur_i, cur_j = queue.popleft()

                        # distance > 0 to make sure this 1 is not the one from first island
                        if grid[cur_i][cur_j] == 1 and distance > 0:
                            return distance -1
                        
                        for d in directions:
                            new_i = cur_i + d[0]
                            new_j = cur_j + d[1]

                            if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in seen:
                                queue.append((new_i, new_j))
                                seen.add((new_i, new_j))

                    distance += 1

        return distance
    
    # return grid

print(
    shortestBridge(grid)
)