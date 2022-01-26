"""
# https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""

from typing import Counter

nums = [1,1,2]

def permuteUnique(nums):
    results = []
    def backtrack(comb, counter):
        if len(comb) == len(nums):
            # make a deep copy of the resulting permutation,
            # since the permutation would be backtracked later.
            results.append(list(comb))
            return

        for num in counter:
            if counter[num] > 0:
                # add this number into the current combination
                comb.append(num)
                counter[num] -= 1
                # continue the exploration
                backtrack(comb, counter)
                # revert the choice for the next exploration
                comb.pop()
                counter[num] += 1

    backtrack([], Counter(nums))

    return results


print(
    permuteUnique(nums)
)