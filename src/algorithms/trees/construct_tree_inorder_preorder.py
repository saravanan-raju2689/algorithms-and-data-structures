def construct_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)

    root_index_in_inorder = inorder.index(root_value)

    root.left = construct_tree(preorder[1:1 + root_index_in_inorder], inorder[:root_index_in_inorder])
    root.right = construct_tree(preorder[1 + root_index_in_inorder:], inorder[root_index_in_inorder + 1:])

    return root

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Explanation:
# This function constructs a binary tree from its preorder and inorder traversals.
# The first element of the preorder list is the root of the tree. 
# We find the index of this root in the inorder list to determine the left and right subtrees.
# The left subtree consists of elements before the root in the inorder list, 
# and the right subtree consists of elements after the root.

# Time Complexity: O(n), where n is the number of nodes in the tree. 
# This is because we visit each node exactly once.