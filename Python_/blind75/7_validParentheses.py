"""
# https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
"""
# s = "()[]{}"
s = "]"

def isValid(s):
    stack = []
    check = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    
    for c in s:
        if c in check:
            if stack and stack[-1] == check[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return True if not stack else False

print(isValid(s))