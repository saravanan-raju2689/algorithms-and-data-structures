def nodes_between_levels(root, level1, level2):
    if not root:
        return []

    result = []
    queue = [(root, 1)]  # (node, current_level)

    while queue:
        node, level = queue.pop(0)

        if level1 <= level <= level2:
            result.append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return result

# Explanation:
# This function prints all nodes between two given levels in a binary tree.
# It uses a level order traversal approach with a queue to keep track of nodes and their levels.
# The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.