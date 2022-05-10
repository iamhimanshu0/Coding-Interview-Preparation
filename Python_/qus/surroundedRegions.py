"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]

Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Input: board = [["X"]]
Output: [["X"]]
"""

board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

def solve(board):
    
    if not board: return []

    row, col = len(board), len(board[0])

    def dfs(i,j):
        if i<0 or i>= row or j<0 or j>= col or board[i][j] != 'O':
            return 
        board[i][j] = "T"

        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i-1,j)
        dfs(i+1,j)

    for r in range(row):
        for c in range(col):
            if board[r][c] == "O" and r in [0, row-1] or c in [0, col-1]:
                dfs(r,c)

    # change O to X
    for r in range(row):
        for c in range(col):
            if board[r][c] == "O":
                board[r][c] = "X"
    
    # change T to O
    for r in range(row):
        for c in range(col):
            if board[r][c] == "T":
                board[r][c] = "O"
    return board



print(
    solve(board)
)