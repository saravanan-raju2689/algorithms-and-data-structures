def check_bst(root):
    def is_bst(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (is_bst(node.left, min_val, node.val) and
                is_bst(node.right, node.val, max_val))

    return is_bst(root, float('-inf'), float('inf'))