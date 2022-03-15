"""
# https://leetcode.com/problems/jump-game-iii/

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
"""

arr = [4,2,3,0,3,1,2]; start = 5

def canReach(arr, start):
    stack = []
    stack.append(start)

    seen = set()
    seen.add(start)

    while stack:
        initPos = stack.pop()
        # check if we already reached 0
        if arr[initPos]==0:
            return True

        # check it's left anf right child
        left = initPos - arr[initPos]
        right = initPos + arr[initPos]

        # check if left is valid and not in hashset
        if left >= 0 and left < len(arr) and left not in seen:
            seen.add(left)
            stack.append(left)
        
        # check if right is valid and not in hashset
        if right >= 0 and right < len(arr) and right not in seen:
            seen.add(right)
            stack.append(right)

    return False


print(
    canReach(arr, start)
)