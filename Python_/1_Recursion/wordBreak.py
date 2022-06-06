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
s = "leetcode"
wordDict = ["leet","code"]

# s = "catsandog"
# wordDict = ["cats","dog","and","cat"]

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

def wordBreakDP(s, wordDict):
    table = [False for _ in range(len(s)+1)]
    table[0] = True
    
    for i in range(1,len(s)):
        if table[i] == True:
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    table[i+len(word)] == True
    # print(table)
    return table[-1]

def leetCode(s, wordDict):
    n = len(s)
    dp = [False for _ in range(n+1)]
    dp[0] = True

    for i in range(1, n+1):
        for w in wordDict:
            if dp[i-len(w)] and s[i-len(w):i]==w:
                dp[i]=True
    return dp[-1]
            


print(leetCode(s, wordDict))