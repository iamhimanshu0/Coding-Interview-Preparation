"""
# https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

"""
nums = [1,2,3,1]

def findPeak(nums):
    l, r = 0, len(nums)-1

    while l < r - 1:
        mid = (l+r)//2

        if nums[mid] > nums[mid+1] and nums[mid]> nums[mid-1]:
            return mid

        if nums[mid] < nums[mid +1]:
            l = mid +1
        else:
            r = mid -1
        
    return l if nums[l] >= nums[r] else r



print(
    findPeak(nums)
)