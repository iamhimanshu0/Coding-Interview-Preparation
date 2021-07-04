# Rotate matrix - 
# Given an image represented by a NxN matrix 
# write a method to rotate the image by 90 degrees.

import numpy as np 

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print("*"*30)
def rotate_matrix(matrix):
    no_of_rows = len(matrix)

    for layer in range(no_of_rows//2):
        first = layer
        last = no_of_rows - layer -1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right element to the bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top to right
            matrix[i][-layer-1] = top

    return matrix


print(rotate_matrix(arr))

