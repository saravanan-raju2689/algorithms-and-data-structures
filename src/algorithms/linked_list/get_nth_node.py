def get_nth_node(head, n):
    """
    Retrieve the Nth node from a linked list.

    Parameters:
    head (Node): The head of the linked list.
    n (int): The position of the node to retrieve (1-based index).

    Returns:
    Node: The Nth node in the linked list, or None if it doesn't exist.
    """
    current = head
    count = 1

    while current is not None:
        if count == n:
            return current
        count += 1
        current = current.next

    return None  # If the Nth node does not exist


# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using a constant amount of space.