"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""
numCourses = 2
prerequisites = [[1,0],[0,1]]

# o(n+p) == > n = numCourser, p = prerequisites

def canFinish(numCourses, prerequisites):
    # create adj list
    preMap = {i:[] for i in range(numCourses)}
    
    for crs, prereq in prerequisites:
        preMap[crs].append(prereq)

    visited = set()

    def dfs(course):
        if course in visited:
            return False
        
        if preMap[course] == []:
            return True
        
        visited.add(course)

        for node in preMap[course]:
            if not dfs(node): return False

        visited.remove(course)
        preMap[course] = []
        return True
    
    for c in range(numCourses):
        if not dfs(c): return False
    
    return True
        

def canFinish2(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    # create graph
    for pair in prerequisites:
        x,y = pair
        graph[x].append(y)
    
    def dfs(graph,visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        
        # if it is done visited then do not visit again
        if visited[i] == 1:
            return False
        
        # maked as being visited
        visited[i] = -1

        # visit all the neighbour
        for j in graph[i]:
            if not dfs(graph, visited, j):
                return False
        
        # after visit all the neighbour, mark it as done visited
        visited[i] = 1

        return True


    for i in range(numCourses):
        if not dfs(graph, visited, i):
            return False
    return True

    

print(
    canFinish2(numCourses, prerequisites)
)