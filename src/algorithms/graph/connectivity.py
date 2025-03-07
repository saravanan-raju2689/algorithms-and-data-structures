def is_connected(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from the first node in the graph
    start_node = next(iter(graph))
    dfs(start_node)

    # Check if all nodes were visited
    return len(visited) == len(graph)