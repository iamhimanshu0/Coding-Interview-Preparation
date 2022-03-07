"""
# https://leetcode.com/problems/count-sub-islands/

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

"""

"""
IDEA:
    👉 firstly remove all the non-common island
    👉 Now count the sub-islands
"""

grid1 = [[1,1,1,0,0],
         [0,1,1,1,1],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [1,1,0,1,1]]

grid2 = [[1,1,1,0,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,0]]

def countSubIslands(grid1, grid2):
    subIsland = 0    
    r, c = len(grid1), len(grid1[0])

    def dfs(i,j):
        if i <0 or i>=r or j <0 or j >=c or grid2[i][j]==0:
            return

        grid2[i][j] = 0
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i-1,j)

    # removing all the non-common sub-islands
    for i in range(r):
        for j in range(c):
            if grid2[i][j]== 1 and grid1[i][j]==0:
                dfs(i,j)

    # counting sub-islands
    for i in range(r):
        for j in range(c):
            if grid2[i][j]==1:
                dfs(i,j)
                subIsland+=1
    
    return subIsland


print(
    countSubIslands(grid1, grid2)
)