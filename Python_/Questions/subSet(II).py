"""
# https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]
"""

S = [1,2,2]

def subSetWithDuplicates(S):
    res = [[]]
    S.sort()
    for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
            l = len(res)
        for j in range(len(res) - l, len(res)):
            res.append(res[j] + [S[i]])
    return res

print(
    subSetWithDuplicates(S)
)