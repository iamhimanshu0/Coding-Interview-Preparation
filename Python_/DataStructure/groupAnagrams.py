"""
# https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]

# def groupAnagrams(strs):
#     res = defaultdict(list)  # mapping charCount to list of Anagrams

#     for s in strs:
#         count = [0]*26

#         for c in s:
#             count[ord(c) - ord("a")] +=1
        
#         res[tuple(count)].append(s)
    
#     return res.values()


def groupAnagrams(strs):
    anagram = {}
    for word in strs:
        currentWord = "".join(sorted(word))
        if currentWord in anagram:
            anagram[currentWord].append(word)
        else:
            anagram[currentWord] = [word]

    return list(anagram.values())

print(groupAnagrams(strs))