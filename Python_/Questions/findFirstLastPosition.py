"""
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
"""

nums = [5,7,7,8,8,10]
target = 8

def searchRange(nums, target):
    
    # leftBias = [true/false], if false , res in rightBiased
    def binSearch(nums, target, leftBias):
        l, r = 0, len(nums)-1
        i = -1
        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m +1
            elif target < nums[m]:
                r = m -1
            else:
                i = m
                if leftBias:
                    r = m -1
                else:
                    l = m +1
        return i 

    left = binSearch(nums, target, True)
    right = binSearch(nums, target, False)

    return [left, right]

    # return []

# class Solution:
#     def searchRange(self, nums, target):
#         left = self.searchLeftRange(nums, target)
#         right = self.searchRightRange(nums, target)

#         return [left, right]


#     def searchLeftRange(self, nums, target):
#         index  = -1
#         l ,r = 0 , len(nums)-1
#         while l <= r:
#             mid =  (l +r )//2

#             if nums[mid] >= target:
#                 r = mid -1
#             else:
#                 l = mid + 1
                
#             if mid == target:
#                 index = mid
        
#         return index

#     def searchRightRange(self, nums, target):
#         index  = -1
#         l ,r = 0 , len(nums)-1
#         while l <= r:
#             mid =  (l +r )//2

#             if nums[mid] <= target:
#                 l = mid +1
#             else:
#                 r = mid -1
                
#             if mid == target:
#                 index = mid
        
#         return index

# s = Solution()
# print(
#     s.searchRange(nums, target)
# )