def iterative_preorder_traversal(root):
    """
    Perform iterative preorder traversal of a binary tree.

    Args:
    root: TreeNode, the root of the binary tree.

    Returns:
    List[int]: A list of values representing the preorder traversal.
    """
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right child first so that left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree (for the stack).