"""
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Input: nums = [0]
    Output: [0]

    https://leetcode.com/problems/move-zeroes/
"""
nums = [0,1,0,3,12]

# o(n^2)
# def moveZero(nums):
#     for i in range(len(nums)):
#         for j in range(0,i+1):
#             if nums[i] == 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#             if nums[j] == 0:
#                 nums[i], nums[j] = nums[j], nums[i]

#     return nums

def moveZero(nums):
    snowBallSize = 0; 
    for i in range(len(nums)):
        if (nums[i]==0):
            snowBallSize +=1; 

        elif(snowBallSize > 0):
            t = nums[i];
            nums[i]=0;
            nums[i-snowBallSize]=t;
    


def moveZeroSimplePowerFull(nums):
    l = 0 
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
    return nums


print(
    moveZeroSimplePowerFull(nums)
)