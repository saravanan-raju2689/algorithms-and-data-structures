def strongly_connected_components(graph):
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def reverse_graph(graph):
        reversed_graph = {v: [] for v in graph}
        for v in graph:
            for neighbor in graph[v]:
                reversed_graph[neighbor].append(v)
        return reversed_graph

    def dfs_on_reversed(v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in reversed_graph[v]:
            if not visited[neighbor]:
                dfs_on_reversed(neighbor, visited, component)

    stack = []
    visited = {v: False for v in graph}

    for v in graph:
        if not visited[v]:
            dfs(v, visited, stack)

    reversed_graph = reverse_graph(graph)
    visited = {v: False for v in graph}
    scc = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_on_reversed(v, visited, component)
            scc.append(component)

    return scc