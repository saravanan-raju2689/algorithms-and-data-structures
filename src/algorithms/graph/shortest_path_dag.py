def shortest_path_dag(graph, start):
    # Initialize distances from start to all other vertices as infinite
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Perform topological sorting
    topological_order = topological_sort(graph)

    # Relax edges in topological order
    for vertex in topological_order:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[vertex] + weight

    return distances

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]  # Return reversed stack for topological order