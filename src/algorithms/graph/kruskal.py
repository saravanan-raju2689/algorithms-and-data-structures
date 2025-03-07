def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(vertices, edges):
    result = []  # This will store the resultant MST
    i = 0  # Initial index of sorted edges
    e = 0  # Initial index of result[]

    # Step 1: Sort all the edges in non-decreasing order of their weight
    edges = sorted(edges, key=lambda item: item[2])

    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < vertices - 1:
        # Step 2: Pick the smallest edge and increment the index
        u, v, w = edges[i]
        i += 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        # If including this edge does not cause a cycle
        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result

# Explanation:
# Kruskal's algorithm finds the Minimum Spanning Tree (MST) for a connected weighted graph.
# It works by sorting all the edges in non-decreasing order of their weight and adding them one by one to the MST,
# ensuring that no cycles are formed. The algorithm uses a union-find data structure to keep track of connected components.
# 
# Time Complexity: O(E log E), where E is the number of edges. This is due to the sorting step.