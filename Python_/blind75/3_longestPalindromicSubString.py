"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""


def longestPalindrome(self, s):
    self.maxlen = 0
    self.start = 0

    for i in range(len(s)):
        self.expandFromCenter(s,i,i)
        self.expandFromCenter(s,i,i+1)
    return s[self.start:self.start+self.maxlen]


def expandFromCenter(self,s,l,r):
    while l > -1 and r < len(s) and s[l] ==s[r]:
        l -= 1
        r += 1

    if self.maxlen < r-l-1:
        self.maxlen = r-l-1
        self.start = l + 1
    