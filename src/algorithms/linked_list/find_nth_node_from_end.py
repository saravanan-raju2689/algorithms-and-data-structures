def find_nth_node_from_end(head, n):
    """
    Function to find the Nth node from the end of a linked list.
    
    :param head: The head node of the linked list.
    :param n: The position from the end of the linked list.
    :return: The Nth node from the end or None if it doesn't exist.
    """
    main_ptr = head
    ref_ptr = head
    
    # Move ref_ptr to n nodes ahead
    for _ in range(n):
        if ref_ptr is None:
            return None  # n is greater than the number of nodes
        ref_ptr = ref_ptr.next
    
    # Move both pointers until ref_ptr reaches the end
    while ref_ptr:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
    
    return main_ptr  # main_ptr is now at the Nth node from the end

# Big-O Analysis:
# Time Complexity: O(L), where L is the length of the linked list.
# Space Complexity: O(1), as we are using only a constant amount of space.