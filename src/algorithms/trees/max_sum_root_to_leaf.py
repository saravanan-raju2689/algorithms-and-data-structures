def max_sum_root_to_leaf(root):
    if not root:
        return 0

    # Helper function to find the maximum sum
    def max_sum_helper(node, current_sum):
        if not node:
            return current_sum
        
        current_sum += node.val
        
        # If it's a leaf node, return the current sum
        if not node.left and not node.right:
            return current_sum
        
        # Recur for left and right subtrees and return the maximum
        return max(max_sum_helper(node.left, current_sum), 
                   max_sum_helper(node.right, current_sum))

    return max_sum_helper(root, 0)

# Explanation:
# This function calculates the maximum sum from root to leaf in a binary tree.
# It uses a recursive helper function to traverse the tree and keep track of the current sum.
# When a leaf node is reached, it returns the current sum, and the maximum of the sums from both
# left and right subtrees is returned.

# Time Complexity: O(n), where n is the number of nodes in the tree.