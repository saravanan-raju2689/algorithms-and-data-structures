def reverse_in_groups(head, k):
    if head is None or k <= 0:
        return None

    current = head
    prev = None
    count = 0

    # Count the number of nodes in the linked list
    temp = head
    while temp and count < k:
        temp = temp.next
        count += 1

    # If we have k nodes, then reverse them
    if count == k:
        # Reverse the first k nodes
        while count > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count -= 1

        # Now head points to the kth node. Recursively call for the rest of the list
        if next_node:
            head.next = reverse_in_groups(next_node, k)

        # prev is now the new head of the reversed group
        return prev

    # If we don't have k nodes, return head as it is
    return head

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the list once to reverse the nodes in groups.
# Space Complexity: O(1), as we are using a constant amount of space for pointers.