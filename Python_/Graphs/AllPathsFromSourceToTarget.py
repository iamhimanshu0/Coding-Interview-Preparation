"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""
graph = [[1,2],[3],[3],[]]

def allPathsSourceTarget(graph):
    result = {}

    for i, nodes in enumerate(graph):
        if i not in result:
            result[i] = nodes
        else:
            result[i].append(nodes)

    n = len(graph)
    stack = [(0,[0])] # store node and the path leading to it
    res = []

    while stack:
        node, path = stack.pop(0)
        # check leaf
        if node == n -1:
            res.append(path)
        # traverse rest
        for nei in result[node]:
            stack.append((nei, path+[nei]))

    return res
        
def allpathsfromsource(graph):
    def dfs(cur, path):
        if cur == len(graph) - 1: res.append(path)
        else:
            for i in graph[cur]: dfs(i, path + [i])
    res = []
    dfs(0, [0])
    return res
        
print(
    allPathsSourceTarget(graph)
)