# FILE: /python-algorithms-project/python-algorithms-project/src/trees/level_order_traversal.py

"""
Level Order Traversal of a Binary Tree

This implementation performs a level order traversal of a binary tree using a queue.
In level order traversal, nodes are visited level by level from top to bottom and left to right.

Time Complexity: O(n), where n is the number of nodes in the tree.
"""

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

# Example usage:
# Constructing a binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
#
# print(level_order_traversal(root))  # Output: [[1], [2, 3], [4, 5]]