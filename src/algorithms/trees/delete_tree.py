def delete_tree(node):
    if node is None:
        return
    
    # Recursively delete left and right subtrees
    delete_tree(node.left)
    delete_tree(node.right)
    
    # Delete the current node
    del node

# Explanation:
# The delete_tree function takes a node of a binary tree as input and recursively deletes
# all its child nodes before deleting the node itself. This ensures that all memory
# allocated for the tree is freed.

# Big-O Analysis:
# The time complexity of this function is O(n), where n is the number of nodes in the tree,
# because we visit each node exactly once. The space complexity is O(h), where h is the height
# of the tree, due to the recursion stack. In the worst case (for a skewed tree), h can be equal to n.