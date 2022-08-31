"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def duplicated(nums):
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


print(
    duplicated([1,1,1,3,3,4,3,2,4,2])
)
