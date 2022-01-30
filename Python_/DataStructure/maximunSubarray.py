"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    
    curSum, largestSum = 0, nums[0]

    for c in nums:
        curSum = max(c, curSum+c)
        largestSum = max(largestSum, curSum)

    return largestSum

print(
    maxSubArray(nums)
)