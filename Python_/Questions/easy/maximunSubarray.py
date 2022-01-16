"""
# https://leetcode.com/problems/maximum-subarray/

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

# def maxSubArray(nums):
#     maxSub = nums[0]
#     curSum = 0

#     for n in nums:
#         if curSum < 0:
#             curSum = 0
#         curSum += n
#         maxSub = max(maxSub, curSum)
#     return maxSub

# (Kadane's Algorithm)
def maxSubArray(nums):
    curSum, largetSum = 0 , nums[0]
    for c in nums:
        curSum = max(c , curSum + c)
        largetSum = max(largetSum, curSum)

    return largetSum

print(maxSubArray(nums))