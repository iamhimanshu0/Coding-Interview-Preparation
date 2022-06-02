"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
"""

coins = [1,2,5]
amount = 11

def coinChange(coins, amount):
    dp = [0] + [float('inf') for i in range(amount)]
    print(dp)
    for i in range(1, amount+1):
        for coin in coins:
            print(f"i => {i},  coin => {coin},   i-coin  => {i-coin}")
            print(dp)
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)
        print(" ")
    if dp[-1] == float('inf'):
        return -1
    
    return dp[-1]

print(coinChange(coins, amount))