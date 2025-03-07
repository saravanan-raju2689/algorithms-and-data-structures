# FILE: /python-algorithms-project/python-algorithms-project/src/trees/spiral_level_order_traversal.py

"""
Spiral Level Order Traversal of a Binary Tree

This algorithm performs a spiral (or zigzag) level order traversal of a binary tree.
In this traversal, nodes are visited level by level, but the order of traversal alternates
between left-to-right and right-to-left at each level.

Algorithm:
1. Use two stacks to keep track of the current level's nodes and the next level's nodes.
2. Start with the root node in the first stack.
3. While there are nodes in the current stack:
   - Pop nodes from the current stack and push their children onto the next stack.
   - If the current stack is left-to-right, push children from left to right; if right-to-left, push from right to left.
4. Alternate the stacks and repeat until all levels are processed.

Time Complexity: O(n), where n is the number of nodes in the binary tree.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def spiral_level_order_traversal(root):
    if not root:
        return []

    result = []
    current_level = []
    next_level = []
    left_to_right = True

    current_level.append(root)

    while current_level:
        level_values = []
        while current_level:
            node = current_level.pop()
            level_values.append(node.value)

            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

        result.append(level_values)
        current_level, next_level = next_level, current_level
        left_to_right = not left_to_right

    return result
