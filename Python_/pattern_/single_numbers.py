"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
"""


def singleNumber(nums):
    count = {}
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1

    for key, value in count.items():
        if value == 1:
            return key


print(
    singleNumber([4, 1, 2, 1, 2]),
    singleNumber([2, 2, 1]),
    singleNumber([4])

)
