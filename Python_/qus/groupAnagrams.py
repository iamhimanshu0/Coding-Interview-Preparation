"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

"""
strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    hist = {}

    for c in strs:
        key = "".join(sorted(c))
        if key not in hist:
            hist[key] = [c]
        else:
            hist[key] += [c]

    return hist.values()

print(groupAnagrams(strs)) 