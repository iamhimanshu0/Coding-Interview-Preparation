"""
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
"""

nums = [-4,-1,0,3,10]

# o(nlogn)
print(sorted([i*i for i in nums]))


# o(n)
def sortedSquares(nums):
    result = [None] * len(nums)
    initial_indx = 0
    final_indx = len(nums)-1
    insertion_indx = len(nums)-1
    #compare the initial_indx and final_indx
    for _ in range(len(result)):
        if abs(nums[initial_indx]) < abs(nums[final_indx]):
            result[insertion_indx] = nums[final_indx] ** 2
            insertion_indx -= 1
            final_indx -= 1
        else:
            result[insertion_indx] = nums[initial_indx] ** 2
            insertion_indx -= 1
            initial_indx += 1
    return result