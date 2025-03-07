# FILE: /algorithm-project/algorithm-project/src/trees/recursive_tree_traversals.py

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    """Preorder traversal of a binary tree: Root -> Left -> Right"""
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    """Inorder traversal of a binary tree: Left -> Root -> Right"""
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def postorder_traversal(root):
    """Postorder traversal of a binary tree: Left -> Right -> Root"""
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

# Big-O Analysis:
# All three traversals (preorder, inorder, postorder) have a time complexity of O(n),
# where n is the number of nodes in the tree, as each node is visited exactly once.
# The space complexity is O(h) for the recursive call stack, where h is the height of the tree. 
# In the worst case (unbalanced tree), h can be equal to n, leading to O(n) space complexity. 
# In a balanced tree, h would be log(n), leading to O(log n) space complexity.