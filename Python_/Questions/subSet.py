"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
"""

nums = [1,2,3]

def subsets(nums):
    n = len(nums)
    output = [[]]
    
    for num in nums:
        output += [curr + [num] for curr in output]
    
    return output


print(
    subsets(nums)
)