"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def searchMatrix(matrix, target):
    row, COLS = len(matrix), len(matrix[0])

    l , r = 0, row*COLS-1

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