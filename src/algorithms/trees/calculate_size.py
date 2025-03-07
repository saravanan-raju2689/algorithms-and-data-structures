def calculate_size(root):
    """
    Calculate the size of a binary tree.

    Parameters:
    root (Node): The root node of the binary tree.

    Returns:
    int: The total number of nodes in the binary tree.
    """
    if root is None:
        return 0
    else:
        return 1 + calculate_size(root.left) + calculate_size(root.right)

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.
# This is because we visit each node exactly once.
# The space complexity is O(h), where h is the height of the tree, due to the recursion stack.