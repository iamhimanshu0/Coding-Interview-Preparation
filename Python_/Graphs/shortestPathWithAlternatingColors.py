"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the 
length of the shortest path from node 0 to node x such that the 
edge colors alternate along the path, or -1 if such a path does not exist.

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
"""
n = 3; redEdges = [[0,1],[1,2]]; blueEdges = []

def shortestAlternatingPaths(n, redEdges, blueEdges):
    ans,visited=[-1]*n,{(0,'inf')}
    graph=[[] for _ in range(n)]
    for u,v in redEdges:
        graph[u].append((v,1))
    for u,v in blueEdges:
        graph[u].append((v,-1))
    queue=[(0,'inf',0)]
    while queue:
        new=[]
        for node,color,dist in queue:
            if ans[node]==-1:
                ans[node]=dist
            for next_node, new_color in graph[node]:
                if new_color!=color and (next_node,new_color) not in visited:
                    new.append((next_node,new_color,dist+1))
                    visited.add((next_node,new_color))
        queue=new
    return ans

print(shortestAlternatingPaths(n, redEdges, blueEdges))