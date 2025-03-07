def iterative_postorder_traversal(root):
    """
    Perform iterative postorder traversal of a binary tree.

    Args:
    root: TreeNode - The root of the binary tree.

    Returns:
    List[int] - A list of values representing the postorder traversal.
    """
    if not root:
        return []

    stack = []
    output = []
    current = root

    while stack or current:
        if current:
            stack.append(current)
            output.append(current.val)  # Append the root node value
            current = current.right  # Traverse right first
        else:
            current = stack.pop()
            current = current.left  # Then traverse left

    return output[::-1]  # Reverse the output to get postorder

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree (for the stack).