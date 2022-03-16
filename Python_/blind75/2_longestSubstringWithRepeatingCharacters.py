"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
s = "abcabcbb"

def lengthOfLongestSubstring(s):
    charset = set()
    l =0 
    result = 0
    for i in range(len(s)):
        while s[i] in charset:
            charset.remove(s[i])
            l+=1
        charset.add(s[i])
        result = max(result, i-l+1)
    return result

print(lengthOfLongestSubstring(s))
