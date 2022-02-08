"""
# https://leetcode.com/problems/add-digits/

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Input: num = 0
Output: 0
"""
num = 38

def addDigits(num):

    def helper(nums):
        
        while True:
            number = nums%10 + nums//10
            # print(number)
            if len(str(number)) <= 1:
                return number 
                
            nums = number
    
    return helper(num)

    

print(addDigits(num))