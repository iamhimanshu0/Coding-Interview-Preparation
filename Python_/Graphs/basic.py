
graph = {
    "a": ["b", "c"],
    "b": ["d", "c"],
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


def depthFirstTraversal(graph, node):
    stack = [node]

    while len(stack) > 0:
        current = stack.pop()
        print(current, end="-")

        for n in graph[current]:
            stack.append(n)
    print("\n")


def depthFirstTraversalRecurssive(graph, node):
    print(node, end="-")

    for n in graph[node]:
        depthFirstTraversalRecurssive(graph, n)


def BreadthFirstTraversal(graph, node):
    queue = [node]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current, end="-")

        for n in graph[current]:
            queue.append(n)

    print("\n")


# depthFirstTraversal(graph, "a")
# depthFirstTraversalRecurssive(graph, "a")


# BreadthFirstTraversal(graph, "a")
