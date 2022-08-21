"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
"""


def isIsomorphic(s, t):
    mapping_s_t = {}
    mapping_t_s = {}

    for c1, c2 in zip(s, t):
        if c1 not in mapping_s_t and c2 not in mapping_t_s:
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False

    return True


print(
    isIsomorphic("egg", "add"),
    isIsomorphic("foo", "bar"),
    isIsomorphic("paper", "title"),
    isIsomorphic("badc", "baba")
)
