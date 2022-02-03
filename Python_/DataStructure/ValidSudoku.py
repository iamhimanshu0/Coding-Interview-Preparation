"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
import collections


board =  [[".","8","7","6","5","4","3","2","1"],
          ["2",".",".",".",".",".",".",".","."],
          ["3",".",".",".",".",".",".",".","."],
          ["4",".",".",".",".",".",".",".","."],
          ["5",".",".",".",".",".",".",".","."],
          ["6",".",".",".",".",".",".",".","."],
          ["7",".",".",".",".",".",".",".","."],
          ["8",".",".",".",".",".",".",".","."],
          ["9",".",".",".",".",".",".",".","."]]

def isValidSudoku(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.': continue  # as need to check for filled val only

            # determine the square 
            #   -> Each Square is single cell in 3*3 Matrix
            i, j = r//3, c//3
            v = board[r][c]  # curr cell val

            # is duplicate of {v} present in row, col, or Square
            if (v in rows[r]) or (v in cols[c]) or (v in squares[(i,j)]):
                return False 

            # record vals of row, col, sqr
            rows[r].add(v)
            cols[c].add(v)
            squares[(i,j)].add(v)

    return True
            
    

print(
    isValidSudoku(board)
)