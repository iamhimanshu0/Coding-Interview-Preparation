"""
# https://leetcode.com/problems/find-eventual-safe-states/

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
"""

from importlib_metadata import collections


graph = [[1,2],[2,3],[5],[0],[5],[],[]]

def eventualSafeNodes(graph):
    n = len(graph)
    out_degree = collections.defaultdict(int)
    in_nodes = collections.defaultdict(list) 
    queue = []
    ret = []
    for i in range(n):
        out_degree[i] = len(graph[i])
        if out_degree[i]==0:
            queue.append(i)
        for j in graph[i]:
            in_nodes[j].append(i)  
    while queue:
        term_node = queue.pop(0)
        ret.append(term_node)
        for in_node in in_nodes[term_node]:
            out_degree[in_node] -= 1
            if out_degree[in_node]==0:
                queue.append(in_node)
    return sorted(ret)

print(eventualSafeNodes(graph))