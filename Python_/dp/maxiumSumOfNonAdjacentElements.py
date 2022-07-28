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

    # tabulation method (DP)
    def tabulation():
        dp = [-1] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            take = nums[i]
            if i > 1:
                take += dp[i-2]

            nonTake = 0 + dp[i-1]

            dp[i] = max(take, nonTake)

        return dp[-1]

    # space optimization
    def space_optimization():
        prev = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            take = nums[i]
            if i > 1:
                take += prev2

            nonTake = 0 + prev

            curi = max(take, nonTake)
            prev2 = prev
            prev = curi

        return prev

    # return space_optimization()
    # return solve_dp(len(nums)-1)
    return backtrack(len(nums)-1)


def houseRobber2(nums):

    def dp(n):
        prev2 = 0
        prev = nums[0]
        for i in range(1, len(n)):
            if len(n) == 1:
                return n[0]
            pick = n[i]
            if i > 1:
                pick += prev2

            notPick = 0 + prev

            curi = max(pick, notPick)
            prev2 = prev
            prev = curi

        return prev

    return max(dp(nums[:-1]), dp(nums[1:]))


print(
    # maximunNonAdjacentSums([1, 2, 4]),
    # maximunNonAdjacentSums([2, 1, 4, 9])

    houseRobber2([2, 3, 2]),
    houseRobber2([1, 2, 3, 1]),
    houseRobber2([1, 2])
)
