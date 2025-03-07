def is_complete_binary_tree(root):
    if not root:
        return True

    queue = []
    queue.append(root)
    end = False

    while queue:
        current = queue.pop(0)

        if current.left:
            if end:
                return False
            queue.append(current.left)
        else:
            end = True

        if current.right:
            if end:
                return False
            queue.append(current.right)
        else:
            end = True

    return True

# Time Complexity: O(n), where n is the number of nodes in the tree.
# This is because we visit each node exactly once.