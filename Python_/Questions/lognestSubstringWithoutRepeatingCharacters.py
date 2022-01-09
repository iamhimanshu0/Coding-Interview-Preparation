"""
3. Longest Substring Without Repeating Characters
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

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
# n = "bbbbb"
# n = "abcabcbb"
n = "pwwkew"

def lengthOfLongestSubstring(n):
    chatSet = set()
    l = 0
    result = 0
    for r in range(len(n)):
        while n[r] in chatSet:
            chatSet.remove(n[l])
            l+=1
        chatSet.add(n[r])

        result = max(result, r-l+1)
    return result


print(
    lengthOfLongestSubstring(n)
)
