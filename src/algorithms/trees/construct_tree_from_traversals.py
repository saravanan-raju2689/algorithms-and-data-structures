def build_tree(inorder, preorder):
    if not inorder or not preorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)

    root_index = inorder.index(root_value)

    root.left = build_tree(inorder[:root_index], preorder[1:root_index + 1])
    root.right = build_tree(inorder[root_index + 1:], preorder[root_index + 1:])

    return root

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(inorder, preorder):
    """
    Constructs a binary tree from given inorder and preorder traversal sequences.

    Parameters:
    inorder (list): The inorder traversal of the tree.
    preorder (list): The preorder traversal of the tree.

    Returns:
    TreeNode: The root of the constructed binary tree.
    """
    return build_tree(inorder, preorder)

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.
# This is because we visit each node exactly once.
# The space complexity is O(n) as well, due to the recursion stack and the storage of the tree nodes.