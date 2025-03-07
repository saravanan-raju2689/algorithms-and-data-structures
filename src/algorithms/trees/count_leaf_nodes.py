def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Explanation:
# This function counts the number of leaf nodes in a binary tree.
# A leaf node is defined as a node that does not have any children.
# The function uses a recursive approach to traverse the tree and count the leaf nodes.

# Time Complexity:
# The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.
# This is because we visit each node exactly once.