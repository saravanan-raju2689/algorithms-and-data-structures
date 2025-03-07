def reverse_linked_list(head):
    """
    Reverses a singly linked list.

    :param head: The head node of the linked list.
    :return: The new head node of the reversed linked list.
    """
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to next node

    return prev  # New head of the reversed linked list

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using a constant amount of space.