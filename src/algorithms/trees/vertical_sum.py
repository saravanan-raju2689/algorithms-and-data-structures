def vertical_sum(root):
    if not root:
        return {}

    from collections import defaultdict, deque

    # Dictionary to hold the vertical sums
    vertical_sums = defaultdict(int)
    # Queue for level order traversal
    queue = deque([(root, 0)])  # (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()
        vertical_sums[hd] += node.val

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort the dictionary by horizontal distance and return the sums
    return dict(sorted(vertical_sums.items()))

# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# This is because we visit each node exactly once.
# Space Complexity: O(n) for the queue and the vertical sums dictionary in the worst case.