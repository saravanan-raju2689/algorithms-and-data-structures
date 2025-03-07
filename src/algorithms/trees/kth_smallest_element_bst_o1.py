def kth_smallest_element_bst_o1(root, k):
    """
    Find the kth smallest element in a Binary Search Tree (BST) using O(1) space.
    
    The algorithm uses an iterative approach with a stack to traverse the tree in 
    in-order fashion. It keeps track of the count of nodes visited and returns the 
    kth smallest element when the count matches k.
    
    Time Complexity: O(h + k), where h is the height of the tree.
    Space Complexity: O(1)
    """
    current = root
    count = 0
    stack = []

    while True:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        if not stack:
            return None  # If the stack is empty, we have traversed all nodes
        
        current = stack.pop()
        count += 1
        
        # If count is equal to k, we found our kth smallest element
        if count == k:
            return current.val
        
        # Move to the right node
        current = current.right