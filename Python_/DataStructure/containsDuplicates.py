"""
# https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

nums = [1,2,3,1]

def containsDuplicate(nums):
    check = {}
    for n in range(len(nums)):
        if nums[n] in check:
            return True
        else:
            check[nums[n]] = 1
  
    return False

print(containsDuplicate(nums))