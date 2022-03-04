"""
# https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""

nums = [1, 2]; k = 2
# nums = [1,1,1,2,2,3]; k = 2

def topKFrequent(nums, k):
    if k == len(nums):
        return nums
    check = {}

    for i in range(len(nums)):
        if nums[i] not in check:
            check[nums[i]] =1
        else:
            check[nums[i]] +=1
    result = {k:v for k,v in sorted(check.items(), key=lambda item:item[1])}
    
    return list(result.values())[:k]

print(
    topKFrequent(nums, k)
)