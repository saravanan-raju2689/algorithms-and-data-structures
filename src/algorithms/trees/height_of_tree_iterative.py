def height_of_tree_iterative(root):
    if root is None:
        return 0

    stack = [(root, 1)]
    height = 0

    while stack:
        node, level = stack.pop()
        if node:
            height = max(height, level)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

    return height

# Explanation:
# This function calculates the height of a binary tree iteratively using a stack.
# It traverses the tree and keeps track of the current level. The maximum level
# reached during the traversal is the height of the tree.

# Time Complexity: O(n), where n is the number of nodes in the tree.