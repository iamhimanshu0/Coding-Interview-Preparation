"""
# https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261

You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list.
"""


def maximunNonAdjacentSums(nums):

    def backtrack(idx):
        if idx < 0:
            return 0

        if idx == 0:
            return nums[idx]

        pick = backtrack(idx-2) + nums[idx]
        notPick = backtrack(idx-1) + 0

        return max(pick, notPick)

    return backtrack(len(nums)-1)


print(
    maximunNonAdjacentSums([1, 2, 4])
)
