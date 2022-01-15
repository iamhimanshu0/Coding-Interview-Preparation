"""
# https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""
s = "anargam"
t = "nagaram"

# def isAnagram(s, t):
#     source = {}
#     target = {}
    
#     for i in range(len(s)):
#         if s[i] in source:
#             source[s[i]] +=1
#         else:
#             source[s[i]] = 1

#     for i in range(len(t)):
#         if t[i] in target:
#             target[t[i]] +=1
#         else:
#             target[t[i]] = 1
    
#     return source == target
    
def isAnagram(s,t):
    s,t = list(s), list(t)
    s.sort()
    t.sort()
    return "".join(s) == "".join(t)

print(
    isAnagram(s,t)
)