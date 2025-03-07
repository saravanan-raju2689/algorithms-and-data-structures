def vertical_sum(root):
    if not root:
        return {}

    from collections import defaultdict, deque

    vertical_sums = defaultdict(int)
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