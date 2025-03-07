def height_of_tree(node):
    if node is None:
        return -1  # Return -1 for null nodes to count height correctly

    # Recursively find the height of left and right subtrees
    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)

    # The height of the tree is the maximum of the heights of the subtrees plus one for the current node
    return max(left_height, right_height) + 1

# Explanation:
# This function calculates the height of a binary tree. The height is defined as the number of edges in the longest path from the root to a leaf node.
# The function uses recursion to traverse the tree and calculate the height of the left and right subtrees, returning the maximum height plus one for the current node.

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the number of nodes in the tree, as each node is visited once.
# The space complexity is O(h), where h is the height of the tree, due to the recursion stack. In the worst case (unbalanced tree), this can be O(n).