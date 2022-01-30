"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""

s = "babad"

def longestPalindrome(s):
    res  = ""
    resLen = 0

    for i in range(len(s)):
        # odd length 
        l,r = i ,i 
        while l >=0 and r <len(s) and s[l] == s[r]:
            if (r - l +1)> resLen:
                res = s[l:r+1]
                resLen = r - 1 +1
            l-=1
            r +=1

        # even length 
        l,r = i, i+1
        while l >=0 and r <len(s) and s[l] == s[r]:
            if (r - l +1)> resLen:
                res = s[l:r+1]
                resLen = r - 1 +1
            l-=1
            r +=1

    return res


print(
    longestPalindrome(s)
)