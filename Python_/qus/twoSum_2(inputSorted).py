"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

numbers = [2,7,11,15]
target = 9

# numbers = [2,3,4]; target = 6

# o(n^2)
def twoSum(numbers, target):
    for i in range(len(numbers)):
        find = target - numbers[i]
        for j in range(i+1, len(numbers)):
            if numbers[j] == find:
                return [i+1,j+1]
            elif numbers[j] > find:
                break
    
    return -1

# o(n)
def twoSum2(numbers, target):
    low, high = 0, len(numbers)-1
    while low < high:
        mid = numbers[low] + numbers[high]
        if mid == target:
            return [low+1, high+1]
        elif mid > target:
            high -=1
        else:
            low +=1
   

def twoSumHas(numbers, target):
    result = {}
    for i, v in enumerate(numbers):
        n = target - v
        if n in result:
            return [result[n], i]
        else:
            result[v] = i

            

print(twoSum2(numbers,target))