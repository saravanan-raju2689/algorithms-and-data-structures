def print_middle(head):
    if head is None:
        return None

    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr

# Explanation:
# The function uses the two-pointer technique to find the middle node of a linked list.
# The 'slow_ptr' moves one step at a time, while the 'fast_ptr' moves two steps at a time.
# When 'fast_ptr' reaches the end of the list, 'slow_ptr' will be at the middle.

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using only a constant amount of space.