"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Input: n = 1
Output: [["Q"]]
"""

def isSafe(row, column, n, board):
    
    # check in the row if Q is present or not
    for i in range(n):
        if board[row][i] == "Q":
            return False
    
    # check in the upper diagonal
    i, j = row, column
    while(i>=0 and j>=0):
        if board[i][j] == 'Q':
            return False
        i-=1
        j-=1

    # check lower diagonal
    i,j = row, column
    while i<n and j>=0:
        if board[i][j] == "Q":
            return False
        i+=1
        j-=1

    return True
    

def solveQueens(column, n, board, result):
    if column == n:
        result.append(["".join(i) for i in board])
        return

    for row in range(n):
        if isSafe(row, column, n, board):
            board[row][column] = "Q"
            solveQueens(column+1, n, board, result)
            board[row][column] = "."

    return     

def solveNQueens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    result = []

    solveQueens(0, n, board, result)
    return result

print(
    solveNQueens(4)
)