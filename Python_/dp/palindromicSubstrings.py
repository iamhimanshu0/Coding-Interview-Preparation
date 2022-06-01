"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
s = "abc"

def countSubstrings(s):
    count = 0
    matrix = [[0 for _ in range(len(s))] for _ in range(len(s))]
    
    for i in range(len(s)):
        matrix[i][i] = 1
        count+=1

    for col in range(1, len(s)):
        for row in range(col):
            if row == col-1 and s[col] == s[row]:
                matrix[row][col] = 1
                count+=1
            elif matrix[row+1][col-1] == 1 and s[col]==s[row]:
                matrix[row][col]=1
                count+=1

    return count

print(
    countSubstrings(s)
)