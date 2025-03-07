def print_reverse(head):
    """
    Function to print the elements of a linked list in reverse order.
    
    Parameters:
    head (Node): The head node of the linked list.
    
    Returns:
    None
    """
    if head is None:
        return
    
    # Recursively call the function for the next node
    print_reverse(head.next)
    
    # Print the data of the current node
    print(head.data)

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), due to the recursive call stack.