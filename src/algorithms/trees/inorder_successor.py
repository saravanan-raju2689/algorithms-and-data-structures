class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder_successor(root, n):
    # Base case
    if root is None:
        return None

    # If the value of the current node is greater than the value of n,
    # then the successor lies in the left subtree.
    if n.val < root.val:
        return inorder_successor(root.left, n) or root

    # If the value of the current node is less than or equal to the value of n,
    # then the successor lies in the right subtree.
    return inorder_successor(root.right, n)


def find_inorder_successors(root):
    successors = {}

    def helper(node):
        if node is None:
            return
        helper(node.left)
        if node.left:
            successors[node] = inorder_successor(root, node.left)
        if node.right:
            successors[node] = inorder_successor(root, node.right)
        helper(node.right)

    helper(root)
    return successors


# Example usage
if __name__ == "__main__":
    # Constructing a simple BST
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)
    root.right.right = TreeNode(35)

    successors = find_inorder_successors(root)
    for node, succ in successors.items():
        print(f"Inorder Successor of {node.val} is {succ.val if succ else None}")

# Time Complexity: O(n), where n is the number of nodes in the BST.
# This is because we may need to visit each node to find its successor.