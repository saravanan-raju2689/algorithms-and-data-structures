class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lowest_common_ancestor(root, node1, node2):
    """
    Find the lowest common ancestor (LCA) of two nodes in a binary tree.

    The LCA is defined as the lowest node in the tree that has both 
    node1 and node2 as descendants (where we allow a node to be a 
    descendant of itself).

    Time Complexity: O(n), where n is the number of nodes in the tree.
    Space Complexity: O(h), where h is the height of the tree due to 
    recursion stack.
    """
    if root is None:
        return None

    # If either node1 or node2 matches the root's value, return root
    if root.value == node1 or root.value == node2:
        return root

    # Look for keys in left and right subtrees
    left_lca = lowest_common_ancestor(root.left, node1, node2)
    right_lca = lowest_common_ancestor(root.right, node1, node2)

    # If both of the above calls return Non-NULL, then one key is 
    # present in one subtree and the other is present in the other subtree.
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca

# Example usage:
# Constructing a simple binary tree
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

lca = lowest_common_ancestor(root, 5, 1)
if lca:
    print(f"The LCA of 5 and 1 is: {lca.value}")
else:
    print("LCA not found.")