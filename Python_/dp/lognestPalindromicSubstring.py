"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""
s = "babad"

def longestPalindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    
    longest_palindrome_start, longest_palindrome_len = 0,1

    for end in range(0,n):
        for start in range(end-1,-1,-1):
            # print(f"start :- {start}, end :{end}")
            if s[start] == s[end]:
                if end - start == 1 or dp[start+1][end-1]:
                    print(s[start:end+1])
                    dp[start][end] = True
                    palindrome_len = end - start +1

                    if longest_palindrome_len < palindrome_len:
                        longest_palindrome_start = start
                        longest_palindrome_len = palindrome_len
                        
    return s[longest_palindrome_start: longest_palindrome_start+longest_palindrome_len]

print(
    longestPalindrome(s)
)