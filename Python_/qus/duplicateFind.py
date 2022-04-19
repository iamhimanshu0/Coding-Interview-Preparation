"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3
"""

nums = [1,3,4,2,2]

def duplicate(nums):
    check = {}
    for i in nums:
        if i in check:
            return i
        else:
            check[i] = 1

print(duplicate(nums))