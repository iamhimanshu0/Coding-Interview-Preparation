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

    def find(idx, arr, s):
        if idx == len(s):
            output.append(arr[:])
            return

        for i in range(idx, len(s)):
            if s[:i]== s[:i][::-1]:
                arr.append(s[:i])
                find(i+1, arr, s)
                arr.pop()
       
    
    find(0,[], s)
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
    partition_2("aab")
    # partition("aabb")
)