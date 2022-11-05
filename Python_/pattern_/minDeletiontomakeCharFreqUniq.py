"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Input: s = "aab"
Output: 0
Explanation: s is already good.

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
"""


def minDeletions(s):
    # s = "".join(sorted(s))

    freq = {}
    for i in range(len(s)):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1

    # return freq
    seen = set()
    count = 0

    for _, v in freq.items():
        while v > 0 and v in seen:
            v -= 1
            count += 1

        seen.add(v)

    return count


print(
    minDeletions("aab"),
    minDeletions("aaabbbcc"),
    minDeletions("ceabaacb")
)
