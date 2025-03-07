def convert_to_mirror_tree(root):
    """
    Convert a binary tree to its mirror tree.

    A mirror tree is a tree that is a reflection of the original tree. 
    This function recursively swaps the left and right children of each node.

    Parameters:
    root (Node): The root of the binary tree.

    Returns:
    Node: The root of the mirrored binary tree.
    """
    if root is None:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively call the function on the left and right subtrees
    convert_to_mirror_tree(root.left)
    convert_to_mirror_tree(root.right)

    return root

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the tree. 
# Each node is visited once.
# Space Complexity: O(h), where h is the height of the tree. 
# This is due to the recursive call stack. In the worst case (unbalanced tree), 
# the height could be n, leading to O(n) space complexity. In the best case (balanced tree), 
# it would be O(log n).