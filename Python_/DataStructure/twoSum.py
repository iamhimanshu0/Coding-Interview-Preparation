"""
# https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""

nums = [7,4,15]
target = 11


def twoSum(nums, target):
    d = {}
    for i , n in enumerate(nums):
        value = target - n
        if value in d:
            return [d[value], i]
        else:
            d[n] = i 

    # return nums 


print(
    twoSum(nums, target)
)