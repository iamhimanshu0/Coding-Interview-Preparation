graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
"""
    a ->  c
    |     |
    b < - e
    |
    d - > f
"""

graph2 = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

"""
    f > g > h
    |  /
    i < j
    |
    k
"""

graph3 = {
    "a": ["b"],
    "b": ["c"],
    "c": ["e"],
    "e": ["d", 'f'],
    "d": ["b"],
    "f": []
}
""" 
          c
         / \
    a -> b  e -> f
         \  /
          d
"""


class Graph:
    def __init__(self):
        pass

    # check if we have a path from src node to dst node
    def checkPath(self, graph, src, dst):
        if src == dst:
            return True

        stack = [src]

        while len(stack) > 0:
            current = stack.pop()
            if current == dst:
                return True

            for n in graph[current]:
                stack.append(n)

        return False

    # check if graph contains cycle
    def checkCycle(self, graph, src):
        hasSeen = {}

        stack = [src]

        while len(stack) > 0:
            current = stack.pop()

            if current not in hasSeen:
                hasSeen[current] = 1
            else:
                return True

            for n in graph[current]:
                stack.append(n)

        return False

    def checkCycleRecurssion(self, graph, src):
        pass


# print(Graph().checkPath(graph, "f", "j"))
print(Graph().checkCycle(graph, "a"))
