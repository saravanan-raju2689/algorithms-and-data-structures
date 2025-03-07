def topological_sort(graph):
    from collections import defaultdict, deque

    # Step 1: Calculate in-degrees of all vertices
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Collect all vertices with in-degree 0
    queue = deque([u for u in graph if in_degree[u] == 0])
    top_order = []

    # Step 3: Process vertices
    while queue:
        u = queue.popleft()
        top_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Check if there was a cycle
    if len(top_order) != len(graph):
        raise ValueError("Graph is not a DAG (Directed Acyclic Graph)")

    return top_order