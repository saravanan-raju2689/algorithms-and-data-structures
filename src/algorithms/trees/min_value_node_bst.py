def min_value_node_bst(root):
    """
    This function finds the node with the minimum value in a Binary Search Tree (BST).
    
    The minimum value node is found by traversing the left children of the tree until 
    there are no more left children. This is because, in a BST, the left child is always 
    less than the parent node.

    Time Complexity: O(h), where h is the height of the tree.
    """
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current