def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    def split(head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Merge two sorted linked lists
    def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data < right.data:
            left.next = merge(left.next, right)
            return left
        else:
            right.next = merge(left, right.next)
            return right

    mid = split(head)
    left = head
    right = mid.next
    mid.next = None

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    return merge(left, right)

# Big-O Analysis:
# Time Complexity: O(n log n), where n is the number of nodes in the linked list.
# This is because we are dividing the list into halves (log n) and merging them (n).
# Space Complexity: O(log n) due to the recursive stack space used during the merge sort process.