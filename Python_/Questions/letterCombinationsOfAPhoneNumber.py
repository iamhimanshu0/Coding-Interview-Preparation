"""
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

"""

digits = "23"

def letterCombinations(digits):
    res = []

    buttons = {
        "2":'abc',
        "3":'def',
        "4":'ghi',
        "5":'jkl',
        "6":'mno',
        "7":'pqrs',
        "8":'tuv',
        "9":'wxyz'
    }

    def backtrack(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        
        for c in buttons[digits[i]]:
            backtrack(i+1, curStr+c)

    if digits:
        backtrack(0, "")

    return res

print(
    letterCombinations(digits)
)