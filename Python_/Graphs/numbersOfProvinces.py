"""
# https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""
isConnected = [[1,1,0],[1,1,0],[0,0,1]]

def findCircleNum(isConnected):
    N = len(isConnected)
    seen = set()
    result = 0

    def dfs(node):
        for nei, adj in enumerate(isConnected[node]):
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)

    for i in range(N):
        if i not in seen:
            dfs(i)
            result +=1

    return result

print(
    findCircleNum(isConnected)
)