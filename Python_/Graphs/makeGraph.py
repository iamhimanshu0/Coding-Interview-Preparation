# undirected path

# check if there exist a path for Node A to Node B


edges = [
    ["i", "j"],
    ['k', "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]


def buildGraph(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def hasPath(graph, src, dst, visited):
    if src == dst:
        return True

    # get rid of infinity loop

    if src in visited:
        return False

    visited.add(src)

    for n in graph[src]:
        if hasPath(graph, n, dst) == True:
            return True

    return False


def main():
    graph = buildGraph(edges)

    # visited = set()
    print(hasPath(graph, "i", "o",  set()))


main()
