"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9=15. 
The right to left diagonal = 3+5+9=17. 
Their absolute difference is |15-17| = 2
"""

arr= [
    [1,2,3],
    [4,5,6],
    [9,8,9]
]


def diagonalDifference(arr):
    left_to_right = []
    right_to_left = []
    
    r,c = len(arr), len(arr[0])
    value = 0
    for i in range(r):        
        left_to_right.append(arr[i][value])
        value+=1
    
    value = r
    for j in range(c):
        right_to_left.append(arr[j][value-1])
        value -=1
    
    return abs(sum(right_to_left)- sum(left_to_right))


print(
    diagonalDifference(arr)
)

