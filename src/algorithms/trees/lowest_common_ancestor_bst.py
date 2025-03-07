class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def lowest_common_ancestor_bst(root, n1, n2):
    """
    Find the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).
    
    The LCA is defined as the lowest node in the tree that has both n1 and n2 as descendants.
    In a BST, if both n1 and n2 are smaller than the root, then LCA lies in the left subtree.
    If both n1 and n2 are greater than the root, then LCA lies in the right subtree.
    Otherwise, the root is the LCA.
    
    Time Complexity: O(h), where h is the height of the tree.
    """
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA lies in left subtree
    if n1 < root.val and n2 < root.val:
        return lowest_common_ancestor_bst(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA lies in right subtree
    if n1 > root.val and n2 > root.val:
        return lowest_common_ancestor_bst(root.right, n1, n2)

    return root  # This is the LCA

# Example usage:
# root = TreeNode(20)
# root.left = TreeNode(10)
# root.right = TreeNode(30)
# lca = lowest_common_ancestor_bst(root, 10, 30)
# print("LCA:", lca.val)  # Output: LCA: 20