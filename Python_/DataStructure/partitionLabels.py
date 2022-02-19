"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Input: s = "eccbbbbdec"
Output: [10]
"""
s = "ababcbacadefegdehijhklij"

def partitionLabels(S):
    last = {c: i for i, c in enumerate(S)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
        
    return ans

print(
    partitionLabels(s)
)