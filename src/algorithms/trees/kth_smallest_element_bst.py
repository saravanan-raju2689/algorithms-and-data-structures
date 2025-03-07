def kth_smallest_element_bst(root, k):
    """
    Find the kth smallest element in a Binary Search Tree (BST).
    
    Args:
    root: TreeNode, the root of the BST.
    k: int, the kth position to find the smallest element.
    
    Returns:
    int: the kth smallest element in the BST.
    
    Time Complexity: O(h + k), where h is the height of the tree.
    """
    stack = []
    current = root
    count = 0

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.val
        
        current = current.right
    
    return None  # If k is larger than the number of nodes in the BST.