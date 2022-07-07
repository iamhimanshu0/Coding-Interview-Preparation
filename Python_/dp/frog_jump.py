"""
https://www.codingninjas.com/codestudio/problems/frog-jump_3621012

There is a frog on the 1st step of an N stairs long staircase. The frog wants to reach the Nth stair. HEIGHT[i] is the height of the (i+1)th stair.If Frog jumps from ith to jth stair, the energy lost in the jump is given by |HEIGHT[i-1] - HEIGHT[j-1] |.In the Frog is on ith staircase, he can jump either to (i+1)th stair or to (i+2)th stair. Your task is to find the minimum total energy used by the frog to reach from 1st stair to Nth stair.

If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.
"""


import math


def frogJump(heights):

    def find(idx, memo={}):
        if idx in memo:
            return memo[idx]
        if idx == 0:
            return 0

        rightSide = math.inf

        leftSide = find(idx-1, memo) + abs(heights[idx] - heights[idx-1])

        if idx > 1:
            rightSide = find(idx-2, memo) + abs(heights[idx] - heights[idx-2])

        memo[idx] = min(leftSide, rightSide)
        return memo[idx]

    # return find(len(heights)-1)

    dp = [0 for _ in range(len(heights))]
    dp[0] = 0

    for i in range(1, len(heights)):
        ff = dp[i-1] + abs(heights[i-1] - heights[i])

        ss = math.inf
        if i > 1:
            ss = dp[i-2] + abs(heights[i-2] - heights[i])

        dp[i] = min(ff, ss)

    return dp[-1]


print(
    frogJump([10, 20, 30, 10]),
    frogJump([10, 50, 10]),
    frogJump([7, 4, 4, 2, 6, 6, 3, 4]),
    frogJump([4, 8, 3, 10, 4, 4]),
)
