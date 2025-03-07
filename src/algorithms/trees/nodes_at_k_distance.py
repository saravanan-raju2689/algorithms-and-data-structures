def nodes_at_k_distance(root, k):
    if root is None:
        return

    if k == 0:
        print(root.data)
        return

    nodes_at_k_distance(root.left, k - 1)
    nodes_at_k_distance(root.right, k - 1)

# Explanation:
# This function prints all nodes at a distance k from the root of a binary tree.
# It uses a simple recursive approach to traverse the tree.
# If the current distance k is 0, it prints the node's data.
# Otherwise, it recursively calls itself for the left and right children with k decremented by 1.

# Time Complexity: O(n)
# This is because we may visit all nodes in the tree in the worst case.