# FILE: /python-algorithms-project/python-algorithms-project/src/graph/bfs.py

"""
Breadth-First Search (BFS) Algorithm

BFS is a graph traversal algorithm that explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level. It uses a queue data structure to keep track of the nodes to be explored.

Time Complexity: O(V + E)
- V is the number of vertices in the graph.
- E is the number of edges in the graph.

Space Complexity: O(V)
- This is due to the storage of the queue and the visited list.
"""

from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes.
    queue = deque([start])  # Initialize a queue with the starting node.

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue.
        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited.
            print(vertex)  # Process the vertex (e.g., print it).
            # Enqueue all unvisited neighbors.
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# bfs(graph, 'A')  # Output: A B C D E F
