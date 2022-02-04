"""
# https://leetcode.com/problems/contiguous-array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

nums = [0,1]

def findMaxLengthBF(nums):
    maxLen = 0
    for i in range(len(nums)):
        zero=ones=0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero+=1
            else:
                ones+=1

            if zero == ones:
                maxLen = max(maxLen, j-i +1)


    return maxLen 

def findMaxLength(nums):
    count = 0
    maxLength = 0 
    table = {0:0}

    for index, num in enumerate(nums,1):
        if num == 0:
            count -=1
        else:
            count +=1
        
        if count in table:
            maxLength = max(maxLength, index - table[count])
        else:
            table[count] = index

    return maxLength




print(
    findMaxLengthBF(nums)
)