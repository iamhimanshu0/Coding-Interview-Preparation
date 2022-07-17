"""
# https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261

You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list.
"""


def maximunNonAdjacentSums(nums):

    def backtrack(idx, memo={}):
        if nums[idx] in memo:
            return memo[idx]
        elif idx < 0:
            return 0

        if idx == 0:
            return nums[idx]

        pick = backtrack(idx-2, memo) + nums[idx]
        notPick = backtrack(idx-1, memo) + 0

        memo[idx] = max(pick, notPick)
        return memo[idx]

    return backtrack(len(nums)-1)


print(
    # maximunNonAdjacentSums([1, 2, 4]),
    maximunNonAdjacentSums([1, 2, 4, 3])
)
