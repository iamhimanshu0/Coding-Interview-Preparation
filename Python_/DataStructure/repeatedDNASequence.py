"""
# https://leetcode.com/problems/repeated-dna-sequences/

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""
s = "AAAAAAAAAAA"

def findRepeatedDnaSequences(s):
    # return empty list if len is exactly 10
    if len(s) == 10: return []

    subSequence = [] # for storing length 10 subsequences
    i = 0 # for checking index 
    while i+9 < len(s): 
        subSequence.append(s[i:i+10]) # adding all the subsequence of length 10      
        i+=1 # increase index + 1

    # print(subSequence)

    check = {} # for sotring the occurance
    for word in subSequence:
        if word in check: # if word already in hashmap 
            check[word] +=1 # add one in the count
        else:
            check[word] = 1 # add word in hashmap

    # print(check)

    result = [] # sotring the result
    for key, value in check.items(): # loop through items inside the hashmap
        if value >= 2: # check if occurance
            result.append(key) # add on result

    return result

print(findRepeatedDnaSequences(s))