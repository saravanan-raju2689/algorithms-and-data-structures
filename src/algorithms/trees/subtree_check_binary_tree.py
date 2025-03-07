def is_subtree(s, t):
    if not s:
        return False
    if is_same_tree(s, t):
        return True
    return is_subtree(s.left, t) or is_subtree(s.right, t)

def is_same_tree(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return (s.val == t.val) and is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)

# Time Complexity: O(n * m), where n is the number of nodes in the main tree and m is the number of nodes in the subtree.
# This is because for each node in the main tree, we may need to check all nodes in the subtree.