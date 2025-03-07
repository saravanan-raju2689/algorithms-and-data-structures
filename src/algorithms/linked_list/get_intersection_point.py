def get_intersection_point(head1, head2):
    if not head1 or not head2:
        return None

    # Get the lengths of both linked lists
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    len1 = get_length(head1)
    len2 = get_length(head2)

    # Calculate the difference in lengths
    diff = abs(len1 - len2)

    # Move the pointer of the longer list ahead by the difference
    if len1 > len2:
        for _ in range(diff):
            head1 = head1.next
    else:
        for _ in range(diff):
            head2 = head2.next

    # Move both pointers until they collide
    while head1 and head2:
        if head1 == head2:
            return head1  # Intersection point
        head1 = head1.next
        head2 = head2.next

    return None  # No intersection

# Explanation:
# This function finds the intersection point of two linked lists. 
# It first calculates the lengths of both lists and then aligns them 
# by moving the pointer of the longer list ahead by the difference in lengths. 
# Finally, it traverses both lists simultaneously until it finds the intersection point.

# Big-O Analysis:
# Time Complexity: O(N + M), where N and M are the lengths of the two linked lists.
# Space Complexity: O(1), as we are using only a constant amount of space.