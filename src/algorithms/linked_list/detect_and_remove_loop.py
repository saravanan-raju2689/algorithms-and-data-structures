def detect_and_remove_loop(head):
    """
    Detects and removes a loop in a linked list.
    
    Parameters:
    head (Node): The head of the linked list.

    Returns:
    bool: True if a loop was detected and removed, False otherwise.
    """
    slow = head
    fast = head

    # Detect loop using Floyd's Cycle-Finding Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # Loop detected
            break
    else:
        return False  # No loop found

    # Remove loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Find the node just before the start of the loop
    while fast.next != slow:
        fast = fast.next

    fast.next = None  # Remove the loop
    return True  # Loop was detected and removed

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using only a constant amount of space.