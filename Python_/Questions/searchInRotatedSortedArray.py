"""
# https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""
nums = [1]
target = 1

def search(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l+r)//2

        if target < nums[0] < nums[mid]:
            l = mid +1
        elif target >= nums[0] > nums[mid]:
            r = mid 
        elif nums[mid] < target:
            l = mid +1
        elif nums[mid] > target:
            r = mid
        else:
            return mid
    return -1 


print(
    search(nums, target)
)

            

