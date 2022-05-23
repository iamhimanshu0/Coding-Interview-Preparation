"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

nums = [2,7,9,3,1]


# TC :- O(2^N)  := N is the number of elements in rob, in each index we have 2 choice, rob or not rob
# SC :- O(N) :- required by implicit recursive stack. the max depth of recursion can go up to N

def bruteForce(rob,i=0):
    return max(bruteForce(rob,i+1), rob[i]+bruteForce(rob,i+2)) if i < len(rob) else 0


# TC:- O(N) , we only calculate the result for each index once and there are N indexes
# SC:- O(N), required for dp and implicit recursive stack

def memoRob(nums):

    def rob(i, memo={}):
        if i in memo: return memo[i]

        if i < len(nums):
            memo[i] = max(rob(i+1), nums[i]+rob(i+2))
        else:
            memo[i] = 0
        return memo[i]
    
    return rob(0)


def rob(nums):
    if len(nums) == 0: return 0
    length = len(nums)+1
    memo = [0]*length

    memo[0] = 0
    memo[1] = nums[0]

    for i in range(len(nums)):
        val = nums[i]
        memo[i+1] = max(memo[i], memo[i-1]+val)
    
    return memo[-1]

print(
    memoRob(nums)
)