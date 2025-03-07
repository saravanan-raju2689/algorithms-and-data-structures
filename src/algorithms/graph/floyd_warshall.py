def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths 
    between all pairs of vertices in a weighted graph.

    Parameters:
    graph (list of list of floats): A 2D list representing the adjacency matrix of the graph.
                                     Use float('inf') for no direct path between vertices.

    Returns:
    list of list of floats: A 2D list representing the shortest path distances between all pairs of vertices.
    """
    num_vertices = len(graph)
    # Initialize the distance matrix with the input graph
    distance = [row[:] for row in graph]

    # Update the distance matrix
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Time Complexity: O(V^3), where V is the number of vertices in the graph.
# Space Complexity: O(V^2) for the distance matrix.