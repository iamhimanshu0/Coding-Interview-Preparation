"""
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    Input: s = "God Ding"
    Output: "doG gniD"

    # https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

s = "Let's take LeetCode contest"

def reverseWords(s):
    new = ""
    for i in s.split(" "):
        new+=i[::-1]+" "

    return new.rstrip()
print(reverseWords(s))