"""
# https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Input: n = 1, k = 1
Output: [[1]]
"""

def combine(n, k):
  res = []

  def backtrack(start, comb):
    if len(comb) == k:
      res.append(comb.copy())
      return
    
    for i in range(start,n+1 ):
      comb.append(i)
      backtrack(i+1, comb)
      comb.pop()
    
  backtrack(1,[])

n ,k = 4,  2
print(combine(n,k))
































