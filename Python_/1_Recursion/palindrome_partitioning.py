"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]
"""

def partition(s):
    output = []

    def isPalindrome(st):
        return st == st[::-1]

    def find(idx, arr):
        if idx == len(s)+1:
            output.append(arr[:])
            return

        for i in range(idx, len(s)+1):
            if isPalindrome(s[idx-1:i]):
                arr.append(s[idx-1:i])
                find(i+1, arr)
                arr.pop()
       
    
    find(1,[])
    return output

def partition_2(s):
    res = []

    def find(arr, str):
        if str:
            for i in range(1, len(str)+1):
                if str[:i] == str[:i][::-1]:
                    find(arr+[str[:i]], str[i:])
        elif arr:
            res.append(arr)

    find([],s)
    return res

print(
    partition("aab")
    # partition("aabb")
)