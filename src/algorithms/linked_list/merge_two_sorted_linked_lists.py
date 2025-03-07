def merge_two_sorted_linked_lists(l1, l2):
    # Create a dummy node to simplify the merge process
    dummy = ListNode(0)
    tail = dummy

    # Traverse both lists and append the smaller value to the merged list
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # If there are remaining nodes in either list, append them
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    # Return the merged list, which starts from the next of the dummy node
    return dummy.next

# Explanation:
# This function merges two sorted linked lists into one sorted linked list.
# It uses a dummy node to simplify the merging process and a tail pointer
# to keep track of the last node in the merged list. The function iterates
# through both lists, comparing the current nodes and appending the smaller
# one to the merged list. Once one of the lists is exhausted, it appends
# the remaining nodes from the other list.

# Big-O Analysis:
# The time complexity of this algorithm is O(n + m), where n and m are the
# lengths of the two linked lists. This is because we traverse each list
# once. The space complexity is O(1) since we are not using any additional
# data structures that grow with input size.