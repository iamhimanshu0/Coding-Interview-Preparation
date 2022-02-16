"""
# https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""

from turtle import right


matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 5

# def searchMatrix(matrix, target):
#     ROW, COL = len(matrix), len(matrix[0])

#     for i in range(ROW):
#         for j in range(COL):
#             if matrix[i][j] == target:
#                 return True
#     return False

"""
Hint:

Method_#1:

Take advantage of the property with sorted ordering in row and column respectively.

"Searching in sorted element" usually has strong connection with binary search framework.

Think of classical 1D binary search, and built a element search algorithm with range check and 1D binary search.

First, use range check to locate possible candidate row.

Second, launch 1D binary search on each possible candidate row.
"""
def searchMatrix2(matrix, target):
    if not len(matrix) or not len(matrix[0]):
        return False

    h, w = len(matrix), len(matrix[0])

    for row in matrix:
        # print(row[0], target, row[-1])
        if row[0] <= target <= row[-1]:
            # print(row[0], target, row[-1])

            left, right = 0, w-1

            while left <= right:
                mid = left + (right - left) //2

                mid_value = row[mid]
                print(mid_value)
                if target > mid_value:
                    left = mid+1
                elif target < mid_value:
                    right = mid-1
                else:
                    return True
    return False
                
"""
Method_#2:

Again, utilize the property with sorted ordering.

Start iteration from bottom left corner.

If target is larger then current element, then go right next time.
If target is smaller than current element, then go up next time.

If target is current element, then return True

When next move is out of boundary of matrix, return False ( i.e., target does Not exist in matrix)

"""  
def searchMatrix3(matrix, target):
    if not len(matrix) or not len(matrix[0]):
        return False

    h , w = len(matrix), len(matrix[0])  

    # start searching from bottom left corner
    y ,x = h-1, 0  

    while True:
        if y <0 or x>=w:
            break

        current = matrix[y][x]

        if target < current:
            # target is smaller, then go up
            y-=1

        elif target > current:
            # target is larget , then go right
            x+=1

        else:
            # hit target
            return True
    return False



print(
    searchMatrix3(matrix, target)
)