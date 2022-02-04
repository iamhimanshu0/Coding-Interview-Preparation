"""
# https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1

"""
import collections


s = "loveleetcode"

def firstUniqChar(s):
    count = collections.Counter(s)
        
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1

print(
    firstUniqChar(s)
)
