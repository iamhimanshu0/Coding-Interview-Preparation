"""
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""
s = "cbaebabacd"
p = "abc"

def findAnagrams(s, p):
    if len(p) > len(s): return []

    pCount, sCount = {},{}
    for i in range(len(p)):
        pCount[p[i]] = 1+ pCount.get(p[i],0)
        sCount[s[i]] = 1+ sCount.get(s[i],0)

    res = [0] if sCount == pCount else []

    left= 0
    for right in range(len(p), len(s)):
        sCount[s[right]] = 1 + sCount.get(s[right], 0)
        sCount[s[left]] -= 1

        if sCount[s[left]] == 0:
            sCount.pop(s[left])

        left +=1
        if sCount == pCount:
            res.append(left)

    return res



print(
    findAnagrams(s,p)
)