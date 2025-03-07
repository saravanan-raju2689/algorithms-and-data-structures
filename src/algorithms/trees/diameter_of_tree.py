def diameter_of_tree(root):
    if not root:
        return 0

    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1

    def diameter(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        left_diameter = diameter(node.left)
        right_diameter = diameter(node.right)
        return max(left_height + right_height, max(left_diameter, right_diameter))

    return diameter(root)

# Explanation:
# The diameter of a binary tree is the length of the longest path between any two nodes in the tree.
# This path may or may not pass through the root. The algorithm calculates the height of the left and right
# subtrees for each node and keeps track of the maximum diameter found.

# Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.