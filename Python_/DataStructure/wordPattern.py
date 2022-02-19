"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
pattern = "abba";s = "dog cat cat dog"

def wordPattern(pattern, s):
    words, w_to_p = s.split(" "), dict()
    # print(words, w_to_p)

    if len(pattern) != len(words):
        return False
    
    if len(set(pattern)) != len(set(words)):
        return False

    for i in range(len(words)):
        if words[i] not in w_to_p:
            w_to_p[words[i]] = pattern[i]
        elif w_to_p[words[i]] != pattern[i]:
            return False

    # print(w_to_p)
    return True
    

print(wordPattern(pattern, s))