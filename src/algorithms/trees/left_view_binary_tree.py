def left_view_binary_tree(root):
    if not root:
        return []

    result = []
    max_level = [-1]

    def left_view_util(node, level):
        if node is None:
            return

        if level > max_level[0]:
            result.append(node.data)
            max_level[0] = level

        left_view_util(node.left, level + 1)
        left_view_util(node.right, level + 1)

    left_view_util(root, 0)
    return result

# Explanation:
# The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.
# This implementation uses a recursive approach to traverse the tree and keeps track of the maximum level
# reached so far. When a node is encountered at a new level, it is added to the result.

# Time Complexity: O(n), where n is the number of nodes in the binary tree. 
# This is because we visit each node exactly once.