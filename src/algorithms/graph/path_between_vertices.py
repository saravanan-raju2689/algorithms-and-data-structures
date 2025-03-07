def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    if start == end:
        return True
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if has_path(graph, neighbor, end, visited):
                return True
    
    return False

# Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# print(has_path(graph, 'A', 'F'))  # Output: True

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# This is because in the worst case, we may visit all vertices and edges in the graph.