def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if node.data <= min_val or node.data >= max_val:
        return False
    return (is_bst(node.left, min_val, node.data) and
            is_bst(node.right, node.data, max_val))

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_bst(root):
    """
    Check if a binary tree is a Binary Search Tree (BST).
    
    A binary tree is a BST if:
    1. The left subtree of a node contains only nodes with keys less than the node's key.
    2. The right subtree of a node contains only nodes with keys greater than the node's key.
    3. Both the left and right subtrees must also be binary search trees.
    
    Time Complexity: O(n), where n is the number of nodes in the tree.
    """
    return is_bst(root)