"""
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Input: nums = [1,3,5,6], target = 2
    Output: 1

    Input: nums = [1,3,5,6], target = 7
    Output: 4

    https://leetcode.com/problems/search-insert-position/
"""

def serachInset(nums, target):
    l ,r = 0, len(nums)-1

    while l <= r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid 
        
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid +1 

    return l

nums = [1,3,5,6]
target = 2

print(serachInset(nums, target))
