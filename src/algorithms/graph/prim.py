def prim(graph):
    import heapq

    # Number of vertices in the graph
    num_vertices = len(graph)
    
    # Initialize a min-heap
    min_heap = []
    
    # To keep track of vertices included in the MST
    in_mst = [False] * num_vertices
    
    # Start from the first vertex (index 0)
    in_mst[0] = True
    for edge in graph[0]:
        heapq.heappush(min_heap, edge)
    
    mst_edges = []
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        
        if in_mst[v]:
            continue
        
        # Include this edge in the MST
        mst_edges.append((u, v, weight))
        in_mst[v] = True
        
        # Add all edges from the newly included vertex
        for edge in graph[v]:
            if not in_mst[edge[2]]:
                heapq.heappush(min_heap, edge)
    
    return mst_edges