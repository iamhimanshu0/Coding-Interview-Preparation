"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

# nums = [-1,0,3,5,9,12]
# target = 9

nums = [-1,0,3,5,9,12]
target = 2

def search(nums, target):
    l , r = 0, len(nums)-1

    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            r = mid-1
        elif nums[mid] < target:
            l = mid + 1
        
    return -1


print(
    search(nums, target)
)