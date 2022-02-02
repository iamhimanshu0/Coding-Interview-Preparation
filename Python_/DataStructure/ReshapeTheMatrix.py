"""
# https://leetcode.com/problems/reshape-the-matrix/

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""

mat = [[1,2],[3,4]]
r = 1
c = 4

def matrixReshape(mat, r, c):
    outputmat = [[0 for _ in range(c)] for _ in range(r)]
    ROW, COL = len(mat), len(mat[0])

    if (ROW * COL) != (r * c):
        return mat

    row_nums = col_num = 0 
    for i in range(ROW):
        for j in range(COL):
            outputmat[row_nums][col_num] = mat[i][j]
            col_num+=1
            if(col_num == c):
                col_num = 0 
                row_nums +=1

    return outputmat 

def matrixReshapeFormula(mat, r, c):
    outputmat = [[0 for _ in range(c)] for _ in range(r)]
    ROW, COL = len(mat), len(mat[0])

    if (ROW * COL) != (r * c):
        return mat  

    k = 0 
    for i in range(ROW):
        for j in range(COL):
            outputmat[k//c][k%c] = mat[i][j]
            k+=1

    return outputmat

print(
    # matrixReshape(mat, r, c)
    matrixReshapeFormula(mat, r, c)
)