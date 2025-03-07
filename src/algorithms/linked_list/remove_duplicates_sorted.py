def remove_duplicates_sorted(head):
    """
    Remove duplicates from a sorted linked list.
    
    :param head: The head of the sorted linked list.
    :return: The head of the linked list after removing duplicates.
    """
    if head is None:
        return None

    current = head

    while current and current.next:
        if current.data == current.next.data:
            # Skip the next node
            current.next = current.next.next
        else:
            current = current.next

    return head

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the list once, making comparisons and adjustments as needed.
# Space Complexity: O(1), as we are modifying the list in place and not using any additional data structures.