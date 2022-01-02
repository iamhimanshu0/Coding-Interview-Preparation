
# https://leetcode.com/problems/container-with-most-water/

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""


height = [1,8,6,2,5,4,8,3,7]


def container_with_most_water_1(height):
    min_height, max_height, min_idx, max_idx = height[0], height[-1], 0, len(height)-1

    if(max_height < min_height):
         min_height = max_height
         min_idx = max_idx
         max_height = height[0]
         max_idx = 0

    width = len(height)-1
    max_area = min_height * width

    while width > 0 :
        idx = min_idx
        while(height[idx] <= min_height):
            if(min_idx < max_idx):
                idx+=1
            else:
                idx -=1
            width -=1

            if(width < 1):
                break
        
        if(height[idx] > max_height):
            min_height = max_height
            min_idx = max_idx
            max_idx = idx 
            max_height = height[idx]

        else:
            min_idx = idx 
            min_height = height[idx]

        max_area = max(max_area, width*min_height)

    return max_area


def container_with_most_water_2(height):
    left , right = 0 , len(height)-1
    res = 0

    while left < right:
        area = (right - left)*min(height[left], height[right])
        res = max(res, area)

        if height[left] < height[right]:
            left +=1
        else:
            right -=1
        
    return res


print(
    container_with_most_water_2(height)
)