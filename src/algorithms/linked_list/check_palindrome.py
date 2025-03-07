def is_palindrome(head):
    if head is None:
        return True

    slow = head
    fast = head
    prev = None

    # Find the middle of the linked list
    while fast and fast.next:
        fast = fast.next.next
        # Reverse the first half of the linked list
        temp = slow
        slow = slow.next
        temp.next = prev
        prev = temp

    # If the length is odd, skip the middle element
    if fast:
        slow = slow.next

    # Compare the reversed first half with the second half
    while prev and slow:
        if prev.data != slow.data:
            return False
        prev = prev.next
        slow = slow.next

    return True

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using a constant amount of space.