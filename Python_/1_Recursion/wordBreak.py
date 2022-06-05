"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
# s = "leetcode"
# wordDict = ["leet","code"]

s = "catsandog"
wordDict = ["cats","dog","and","cat"]

def wordBreak(s, wordDict, memo={}):

    if s in memo: return memo[s]
    if s == "":
        return True

    for word in wordDict:
        if s.startswith(word):
            leftword = s[len(word):]
            if (wordBreak(leftword, wordDict, memo) == True):
                memo[s] = True
                return memo[s]

    memo[s] = False     
    return memo[s]
print(wordBreak(s, wordDict))