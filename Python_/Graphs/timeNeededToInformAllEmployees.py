"""
# https://leetcode.com/problems/time-needed-to-inform-all-employees/

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
"""

from collections import defaultdict


n = 6; headID = 2; manager = [2,2,-1,2,2,2]; informTime = [0,0,1,0,0,0]

def numOfMinutes(n , headID, manager, informTime):
    graph = defaultdict(list)

    for i in range(len(manager)):
        graph[manager[i]].append(i)

    def dfs(u):
        ans = 0
        for v in graph[u]:
            ans = max(drv) + informTime[u], ans)
        return ans
    
    return dfs(headID)


print(
    numOfMinutes(n, headID, manager, informTime)
)