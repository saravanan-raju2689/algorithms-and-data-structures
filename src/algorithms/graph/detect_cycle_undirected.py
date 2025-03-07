def detect_cycle_undirected(graph):
    def dfs(v, visited, parent):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True
        return False

    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            if dfs(i, visited, -1):
                return True
    return False

# Explanation:
# This function detects cycles in an undirected graph using Depth-First Search (DFS).
# It maintains a visited list to track visited nodes and a parent variable to avoid 
# counting the immediate parent as a cycle.
# The time complexity is O(V + E), where V is the number of vertices and E is the number of edges.