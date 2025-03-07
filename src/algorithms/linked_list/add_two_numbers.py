def add_two_numbers(l1, l2):
    # Initialize a dummy node to build the result list
    dummy = ListNode(0)
    current = dummy
    carry = 0

    # Loop through both linked lists
    while l1 is not None or l2 is not None or carry:
        # Get the values from the current nodes, if they exist
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        # Move to the next nodes
        current = current.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    # Return the next node of the dummy node, which is the head of the result list
    return dummy.next

# Explanation:
# This function takes two linked lists representing two non-negative integers, where each node contains a single digit.
# The digits are stored in reverse order, meaning that the 1's digit is at the head of the list.
# The function adds the two numbers and returns the sum as a linked list in the same reverse order.

# Big-O Analysis:
# Time Complexity: O(max(m, n)), where m and n are the lengths of the two linked lists. 
# We traverse both lists once.
# Space Complexity: O(max(m, n)), for the resulting linked list that stores the sum.