"""
# https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]
"""

rowIndex = 3

def getRow(rowIndex):
    result = [[1]]

    for _ in range(rowIndex):
        previous = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1])+1):
            row.append(previous[j] + previous[j+1])

        result.append(row)

    return result[-1]

print(
    getRow(rowIndex)
)