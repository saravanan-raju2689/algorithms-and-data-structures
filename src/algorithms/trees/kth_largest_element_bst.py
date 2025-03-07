def kth_largest_element_bst(root, k):
    """
    Function to find the kth largest element in a Binary Search Tree (BST).
    
    Args:
    root: TreeNode, the root of the BST.
    k: int, the kth position to find the largest element.
    
    Returns:
    int: the kth largest element in the BST.
    """
    stack = []
    current = root
    count = 0
    
    # Reverse in-order traversal (right, root, left)
    while stack or current:
        while current:
            stack.append(current)
            current = current.right
        
        current = stack.pop()
        count += 1
        
        # If count equals k, we found our kth largest
        if count == k:
            return current.val
        
        current = current.left
    
    return None  # If k is larger than the number of nodes in the tree

# Time Complexity: O(h + k), where h is the height of the tree.
# Space Complexity: O(h), for the stack used in the traversal.