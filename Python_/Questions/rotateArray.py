"""
    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

nums = [1,2,3,4,5,6,7]
k = 3
# nums = [-1,-100,3,99]
# k = 2

def rotation(nums, k):
    # first reverse array
    l,r = 0, len(nums)-1

    k = k % len(nums)

    # reverse whole array
    while l < r:
        nums[l] , nums[r] = nums[r], nums[l]
        l +=1
        r -=1

    # reverse 
    l,r = 0, k-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    
    # reverse k
    l,r = k, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    
    return nums





print(rotation(nums, k))


