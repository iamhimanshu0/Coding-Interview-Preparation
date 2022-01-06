"""
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.

    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

    # https://leetcode.com/problems/reverse-string/
"""

# s = ["H","a","n","n","a","h"]
s = ["h","e","l","l","o"]


def reverseString(s):
    # return s[::-1]
    l , r = 0, len(s)-1

    while l <= r:
        s[l], s[r] = s[r], s[l]
        l,r = l+1, r-1
    return s

print(reverseString(s))