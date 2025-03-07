def kth_smallest_element_bst(root, k):
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.val

        current = current.right

    return None  # If k is larger than the number of nodes in the BST