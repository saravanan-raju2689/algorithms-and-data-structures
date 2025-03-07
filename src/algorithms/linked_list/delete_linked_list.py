def delete_linked_list(head):
    """
    Deletes a linked list and frees up the memory.
    
    Parameters:
    head (Node): The head of the linked list to be deleted.
    
    Returns:
    None
    """
    current = head
    while current:
        next_node = current.next  # Store the next node
        del current  # Free the current node
        current = next_node  # Move to the next node

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using a constant amount of space.