"""
# https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261

You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list.
"""


def maximunNonAdjacentSums(nums):

    def backtrack(idx, memo={}):
        if idx in memo:
            return memo[idx]

        if idx == 0:
            return idx
        if idx < 0:
            return 0

        pick = backtrack(idx-2, memo) + nums[idx]
        notPick = backtrack(idx-1, memo) + 0

        memo[idx] = max(pick, notPick)
        return memo[idx]

    dp = [-1] * len(nums)

    def solve_dp(idx):

        if idx == 0:
            return idx
        if idx < 0:
            return 0
        if dp[idx] != -1:
            return dp[idx]

        pick = nums[idx] + solve_dp(idx-2)

        notPick = 0 + solve_dp(idx-1)

        dp[idx] = max(pick, notPick)

        return dp[idx]

    return solve_dp(len(nums)-1)
    return backtrack(len(nums)-1)


print(
    # maximunNonAdjacentSums([1, 2, 4]),
    maximunNonAdjacentSums([2, 1, 4, 9])
)
