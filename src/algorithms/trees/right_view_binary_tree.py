def right_view(root):
    if not root:
        return []

    right_view_nodes = []
    queue = [(root, 0)]  # Node with its level

    while queue:
        node, level = queue.pop(0)

        # If this is the first node of its level
        if level == len(right_view_nodes):
            right_view_nodes.append(node.data)

        # Add right child first so that the rightmost node is processed first
        if node.right:
            queue.append((node.right, level + 1))
        if node.left:
            queue.append((node.left, level + 1))

    return right_view_nodes

# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the tree, for the queue.