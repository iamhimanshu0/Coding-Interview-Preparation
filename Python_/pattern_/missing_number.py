"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""

"""
    n(n+1)/2

    5(5+1)/2
    5(6)/2
    30/2
    15
"""


def find_missing(nums):
    n = len(nums)
    n_number_sums = n * (n+1)//2

    return abs(sum(nums) - n_number_sums)


print(
    find_missing([3, 0, 1]),
    find_missing([0, 1]),
    find_missing([9, 6, 4, 2, 3, 5, 7, 0, 1])

)
