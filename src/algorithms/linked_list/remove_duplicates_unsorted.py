def remove_duplicates(head):
    if head is None:
        return None

    current = head
    seen = set()
    seen.add(current.data)

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next  # Remove the node
        else:
            seen.add(current.next.data)
            current = current.next

    return head

# Explanation:
# This function removes duplicates from an unsorted linked list. It uses a set to keep track of the values that have already been seen.
# As we traverse the linked list, if we encounter a value that is already in the set, we skip that node by adjusting the pointers.

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.
# Space Complexity: O(n), in the worst case, we may store all the elements in the set if there are no duplicates.