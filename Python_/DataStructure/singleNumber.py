"""
# https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
"""

nums = [4,1,2,1,2]

def singleNumber(nums):
    check = {}

    for n in nums:
        if n in check:
            check[n] +=1
        else:
            check[n] = 1

    for key, value in check.items():
        if value == 1:
            return key
        else:
            continue

# only using constant space
def singleNumber2(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
print(
    singleNumber2(nums)
)