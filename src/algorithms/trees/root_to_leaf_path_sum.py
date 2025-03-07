def has_path_sum(root, sum):
    if not root:
        return sum == 0

    sum -= root.val

    if not root.left and not root.right:  # If it's a leaf node
        return sum == 0

    return has_path_sum(root.left, sum) or has_path_sum(root.right, sum)

# Time Complexity: O(n), where n is the number of nodes in the tree.
# This is because we may need to visit all nodes in the worst case.