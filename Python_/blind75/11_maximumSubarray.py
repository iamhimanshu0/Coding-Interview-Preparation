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

def maximunSum(nums):
    maxTilNow = nums[0]
    currentMax = 0

    for i in nums:
        # print(f'nums, {i}')
        currentMax = max(i,currentMax+i)
        # print(f'current ', currentMax)
        maxTilNow = max(currentMax, maxTilNow) 
        # print(f"maxTilNow ", maxTilNow)        
        
    return maxTilNow

def approch2(nums):
    for i in range(1, len(nums)):
        if nums[i-1] >0:
            nums[i] += nums[i-1]
    return nums

print(approch2(nums))