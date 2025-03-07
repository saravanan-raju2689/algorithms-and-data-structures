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

# Explanation:
# The function `is_subtree` checks if tree `t` is a subtree of tree `s`.
# It does this by checking if the current node of `s` matches the root of `t`.
# If it does, it calls `is_same_tree` to check if the two trees are identical.
# If not, it recursively checks the left and right subtrees of `s`.
# The function `is_same_tree` checks if two trees are identical by comparing their nodes.

# Time Complexity:
# The time complexity of this approach is O(n * m), where n is the number of nodes in tree `s`
# and m is the number of nodes in tree `t`. In the worst case, we may have to check every node in `s`
# for a match with the root of `t`, and for each match, we may have to traverse all nodes in `t`.