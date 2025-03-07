def bfs_applications(graph, start):
    from collections import deque

    def bfs(graph, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []

        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def bfs_shortest_path(graph, start):
        visited = {start: None}
        queue = deque([start])

        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited[neighbor] = vertex
                    queue.append(neighbor)

        return visited

    def bfs_connected_components(graph):
        visited = set()
        components = []

        for vertex in graph:
            if vertex not in visited:
                component = bfs(graph, vertex)
                components.append(component)
                visited.update(component)

        return components

    return {
        "bfs_order": bfs(graph, start),
        "shortest_path": bfs_shortest_path(graph, start),
        "connected_components": bfs_connected_components(graph)
    }