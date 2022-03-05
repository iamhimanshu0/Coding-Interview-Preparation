"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
from ntpath import join
from tabnanny import check
from typing import Counter


s = "Aabb"


def frequencySort(s):
    check = Counter(s)
    print(check)
    s = list(s)
    s.sort(key=lambda x:(-check[x],x))
    return "".join(s)
   

def frequencySort2(s):
    res = ""
    check = Counter(s)
    arr = [[freq, c] for c, freq in check.items()]
    arr.sort(key=lambda x:-x[0])
    for count, word in arr:
        res+=word*count
    return res
    
print(frequencySort2(s))