"""
# https://leetcode.com/problems/01-matrix/
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]

def updateMatrix(mat):
    ROW, COl = len(mat), len(mat[0])
    q = []

    for i in range(ROW):
        for j in range(COl):
            if mat[i][j] == 0:
                q.append((i,j))
            else:
                mat[i][j] = "#"

    for row, col in q:
        for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
            nr = row + dx
            nc = col + dy

            if 0 <= nr < ROW and 0<= nc < COl and mat[nr][nc]== "#":
                mat[nr][nc] = mat[row][col]+1
                q.append((nr, nc))

    return mat

print(
    updateMatrix(mat)
)