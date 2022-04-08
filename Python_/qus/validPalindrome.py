"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
# s = "A man, a plan, a canal: Panama"
s = "0P"

# bets 99.93% online submission | python
def isPalindrome(s):
    
    s = "".join(filter(str.isalnum, s.replace(",", "").replace(" ", "").lower()))
    print(s)
    return s == s[::-1] 

def isPalindrome2(s):
    s = s.lower()
    start, end = 0, len(s)-1

    while start <= end:
        while not s[start].isalnum() and start < end:
            start +=1
        while not s[end].isalnum() and start < end:
            end -=1
        
        if s[start] == s[end]:
            start, end = start+1, end-1
        else:
            return False
    return True



print(isPalindrome2(s))