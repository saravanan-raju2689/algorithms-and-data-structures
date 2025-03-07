def detect_cycle_directed(graph):
    def dfs(v):
        nonlocal has_cycle
        if has_cycle:
            return
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
            elif rec_stack[neighbor]:
                has_cycle = True
                return
        
        rec_stack[v] = False

    visited = [False] * len(graph)
    rec_stack = [False] * len(graph)
    has_cycle = False

    for node in range(len(graph)):
        if not visited[node]:
            dfs(node)

    return has_cycle

# Explanation:
# This function detects cycles in a directed graph using Depth-First Search (DFS).
# It maintains a visited list to track visited nodes and a recursion stack to track the nodes in the current path.
# If a node is revisited while still in the recursion stack, a cycle is detected.

# Time Complexity: O(V + E)
# Where V is the number of vertices and E is the number of edges in the graph.