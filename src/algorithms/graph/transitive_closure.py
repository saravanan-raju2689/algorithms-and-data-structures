def transitive_closure(graph):
    """Computes the transitive closure of a directed graph using the Floyd-Warshall algorithm."""
    n = len(graph)
    closure = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            closure[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure