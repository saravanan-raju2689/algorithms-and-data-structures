def sorted_insert_circular_linked_list(head, data):
    new_node = Node(data)
    
    # Case 1: If the list is empty
    if head is None:
        new_node.next = new_node  # Point to itself
        return new_node

    # Case 2: If the new node needs to be inserted before the head
    if data < head.data:
        # Find the last node
        last = head
        while last.next != head:
            last = last.next
        last.next = new_node
        new_node.next = head
        return new_node  # New node becomes the new head

    # Case 3: Find the appropriate position to insert
    current = head
    while current.next != head and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head  # Return the original head

# Big-O Analysis:
# Time Complexity: O(n) in the worst case, where n is the number of nodes in the circular linked list.
# Space Complexity: O(1) as we are using a constant amount of space for the new node.