"""
# https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4
"""

# heights = [2,1,5,6,2,3]
heights  = [2]

def lagestRectangleArea(heights):
    maxArea =  0
    stack = [] # pair : (index, height)

    for i , h in enumerate(heights):
        start = i 
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i , h in stack:
        maxArea = max(maxArea, h * (len(heights)- i ))
    
    return maxArea



print(
    lagestRectangleArea(heights)
)