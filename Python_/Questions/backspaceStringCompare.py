"""
# https://leetcode.com/problems/backspace-string-compare/

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""

s = "y#fo##f"
t = "y#f#o##f"


def backspaceCompare(s, t):

    def compare(s):
        result =[]
        for i in s:
            if i == "#" and result:
                result.pop()
            elif i != "#":
                result.append(i)
        return result

    return compare(s) == compare(t)


print(
    backspaceCompare(s,t)
)