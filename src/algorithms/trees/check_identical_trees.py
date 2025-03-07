def are_identical_trees(tree1, tree2):
    # Base case: both trees are empty
    if not tree1 and not tree2:
        return True
    
    # If both trees are not empty, check their data and recursively check their subtrees
    if tree1 and tree2:
        return (tree1.data == tree2.data and
                are_identical_trees(tree1.left, tree2.left) and
                are_identical_trees(tree1.right, tree2.right))
    
    # One tree is empty and the other is not
    return False

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the number of nodes in the trees.
# This is because we may need to visit each node in both trees to determine if they are identical.
# The space complexity is O(h), where h is the height of the trees, due to the recursion stack.