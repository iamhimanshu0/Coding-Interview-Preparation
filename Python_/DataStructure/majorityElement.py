"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""
nums = [2,2,1,1,1,2,2]


# using hash map 
def majorityElement(nums):
    n = len(nums)//2
    check = {}
    for i in nums:
        if i in check:
            check[i] +=1
        else:
            check[i] =1
    
    for key , value in check.items():
        if value > n :
            return key

# using sorting
"""
If the elements are sorted in monotonically increasing (or decreasing) order, the majority element can be found at index 
n/2 and n/2+1 incidentally, if n is even).
"""
# TC :- o(nlogn)
# SC :- o(1) or o(n)
def majorityElementSorting(nums):
    nums.sort()
    return nums[len(nums)//2]

print(
    majorityElementSorting(nums)
)