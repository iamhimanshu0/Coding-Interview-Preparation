"""
# https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []
"""
nums = [-1,0,1,2,-1,-4]


def threeSum(nums):
    nums.sort()
    triplates = []

    for i in range(len(nums)-2):
        left = i +1
        right = len(nums)-1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == 0:
                triplates.append([nums[i], nums[left], nums[right]])
                left +=1
                right -=1
            elif currentSum < 0:
                left +=1
            elif currentSum > 0:
                right -=1
    return triplates


print(
    set(threeSum(nums))
)
