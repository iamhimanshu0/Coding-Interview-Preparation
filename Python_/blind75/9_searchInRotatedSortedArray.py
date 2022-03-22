"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""
from operator import indexOf


nums = [4,5,6,7,0,1,2]; target = 0

def oneline(nums):
    return indexOf(nums,target) if target in nums else -1

def search(nums):
    L, H = 0, len(nums)
    while L < H:
        M = (L+H)//2
        if target < nums[0] < nums[M]:
            L = M+1
        elif target >= nums[0] > nums[M]:
            H = M
        elif nums[M] < target:
            L = M+1
        elif nums[M] > target:
            H = M
        else:
            return M
    return -1

def search2(nums):
    n = len(nums)
    left, right = 0, n-1
    
    while left <= right:
        mid = (left + right)//2
        if nums[mid]== target:
            return mid
            
        # if left half is having uniforming incresing curve
        elif nums[mid] >= nums[left]: #middle value is bigger then left
            # check to see if target element in present in left to mid element range
            if target <= nums[mid] and target >= nums[left]:
                right = mid -1
            else:
                left = mid +1
        # if left half is not having uniforming incresing then go to right
        else:
            # check if elememnt in mid, right
            if target >= nums[mid] and target <= nums[right]:
                left = mid +1
            else:
                right = mid -1

    return -1


print(search2(nums))