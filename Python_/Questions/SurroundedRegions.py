"""
# https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Input: board = [["X"]]
Output: [["X"]]
"""

board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]



def solve(board):

    ROW, COL = len(board), len(board[0])

    def capture(r,c):
        if r < 0 or c < 0 or r == ROW or c == COL or board[r][c] != 'O':
            return 
        board[r][c] = "T"

        capture(r+1, c)
        capture(r-1, c)
        capture(r, c+1)
        capture(r, c-1)

    #(DFS)capture unsurrounded regions (O -> T)
    # only checking borders  
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == "O" and r in [0, ROW-1] or c in [0, COL-1]:
                capture(r,c)

    # Capture surrounded regions (O -> X)
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == "O":
                board[r][c] = "X"

    # return board (T -> O)
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == "T":
                board[r][c] = "O"

    return board


print(
    solve(board)
)