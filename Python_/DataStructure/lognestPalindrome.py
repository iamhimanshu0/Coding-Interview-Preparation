"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1

Input: s = "bb"
Output: 2
"""
s = "abccccdd"

def longestPalindrome(s):
    hash = set()

    for c in s:
        if c not in hash:
            hash.add(c)
        else:
            hash.remove(c)

    # print(hash)
    if len(hash) >0:
        return len(s) - len(hash)+1
    else:
        len(s)

print(longestPalindrome(s))