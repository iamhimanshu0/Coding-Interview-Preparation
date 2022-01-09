"""
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.


    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

    https://leetcode.com/problems/permutation-in-string/
"""
s1 = "ab"
s2 = "eidboaoo"

def checkInclusion(s1, s2):
    freq1 = {}
    freq2 = {}

    for i in range(len(s1)):
        if s1[i] not in freq1:
            freq1[s1[i]] = 1
        else:
            freq1[s1[i]] +=1
    
    for i in range(len(s2)):
        if s2[i] not in freq2:
            freq2[s2[i]] = 1
        else:
            freq2[s2[i]] +=1


    for i, v in freq1.items():
        # print(i,v)
        if i in freq2.keys():
            print(v, freq2[i])
            # if v == freq2[i]:
                # return True
        else:
            return False

print(
    checkInclusion(s1, s2)
)