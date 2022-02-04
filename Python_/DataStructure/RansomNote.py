"""
# https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

from tabnanny import check


ransomNote = "aa"
magazine = "aab"

def canConstruct(ransomNote, magazine):

    checkNote ={} 
    checkMagine = {}

    for s in ransomNote:
        if s not in checkNote:
            checkNote[s] =1
        else:
            checkNote[s] +=1

    for i in magazine:
        if i not in checkMagine:
            checkMagine[i] =1
        else:
            checkMagine[i] +=1
    
    for i in checkNote:
        if i not in checkMagine:
            return False
        else:
            if checkNote[i] > checkMagine[i]:
                return False
    return True 

 



print(
    canConstruct(ransomNote, magazine)
)

