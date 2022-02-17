"""
# https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2

"""

nums = [1,1,1]; k = 2

def subarraySum(nums,k):
    ans, n = 0, len(nums)
    preSum = [nums[0]]
    dic = {}
    dic[0] = 1
    for i in nums[1:]:
        preSum.append(i+preSum[-1])
    for i in preSum:
        if i-k in dic:
            ans+=dic[i-k]
        dic[i] = dic.get(i,0) + 1 
    return ans


print(subarraySum(nums,k))