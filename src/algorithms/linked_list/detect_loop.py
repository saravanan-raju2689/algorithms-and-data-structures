def detect_loop(head):
    """
    Detects a loop in a linked list using Floyd's Cycle-Finding Algorithm.
    
    Parameters:
    head (Node): The head node of the linked list.

    Returns:
    bool: True if a loop is detected, False otherwise.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # Move slow pointer by 1
        fast = fast.next.next     # Move fast pointer by 2

        if slow == fast:          # A loop is detected
            return True

    return False                  # No loop detected

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using only two pointers.