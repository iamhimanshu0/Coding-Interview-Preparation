"""
# https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 89

# def searchMatrix(matrix, target):
#     ROW, COL = len(matrix), len(matrix[0])

#     for i in range(ROW):
#         for j in range(COL):
#             if matrix[i][j] == target:
#                 return True
#     return False

# def searchMatrix(matrix, target):
#     ROWS, COLS = len(matrix), len(matrix[0])

#     top, bot = 0, ROWS -1 
#     while top  <= bot:
#         row = (top+bot)//2
#         if target > matrix[row][-1]:
#             top = row +1 
#         elif target < matrix[row][0]:
#             bot = row - 1 
#         else:
#             break

#     if not (top <= bot):
#         return False
    
#     row = (top + bot) //2
#     l, r = 0, COLS -1 
#     while l <= r:
#         m = (l+r) //2 
#         if target > matrix[row][m]:
#             l = m +1
#         elif target > matrix[row][m]:
#             r = m -1
#         else:
#             return True
#     return False


def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    
    l, r = 0, ROWS*COLS - 1

    while l <= r:
        mid = (l+r)//2
        if matrix[mid//COLS][mid%COLS] == target:
            return True
        elif matrix[mid//COLS][mid%COLS] < target:
            l = mid +1
        elif matrix[mid//COLS][mid%COLS] > target:
            r = mid - 1
    return False



print(
    searchMatrix(matrix, target)
)