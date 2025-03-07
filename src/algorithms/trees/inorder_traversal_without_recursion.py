# FILE: /python-algorithms-project/python-algorithms-project/src/trees/inorder_traversal_without_recursion.py

"""
Inorder Traversal Without Recursion

Inorder traversal of a binary tree visits the nodes in the following order:
1. Left subtree
2. Root node
3. Right subtree

This implementation uses a stack to simulate the recursive behavior of the traversal.

Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree due to the stack space.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    stack = []
    current = root
    result = []

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result

# Example usage:
# Constructing a simple binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Inorder Traversal:", inorder_traversal(root))  # Output: [4, 2, 5, 1, 3]