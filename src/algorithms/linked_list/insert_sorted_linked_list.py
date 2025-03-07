def insert_sorted_linked_list(head, new_node):
    """
    Inserts a new node into a sorted linked list.

    Parameters:
    head (Node): The head of the sorted linked list.
    new_node (Node): The new node to be inserted.

    Returns:
    Node: The head of the modified linked list.
    """
    # If the linked list is empty or the new node should be inserted at the head
    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node

    # Traverse the list to find the correct position for the new node
    current = head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    # Insert the new node
    new_node.next = current.next
    current.next = new_node

    return head

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# This is because we may need to traverse the entire list in the worst case.
# Space Complexity: O(1), as we are using a constant amount of space for pointers.