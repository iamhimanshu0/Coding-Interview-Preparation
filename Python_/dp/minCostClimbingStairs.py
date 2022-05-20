"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""
cost = [1,100,1,1,1,100,1,1,100,1]

def minCostRecursion(n, cost):
    dp = [None]*n 
    
    # base case 
    if n ==1:
        return cost[0]
    
    # initially to climb 
    # till 0-th or 1th stair
    dp[0] = cost[0]
    dp[1] = cost[1]

    # iterate for finding the cost
    for i in range(2,n):
        print(dp)
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

    print(dp[n-1], dp[n-2])
    return min(dp[n-2], dp[n-1])

def minCostClimbingStairs(cost):
    return minCostRecursion(len(cost),cost)

print(
    minCostClimbingStairs(cost)
)