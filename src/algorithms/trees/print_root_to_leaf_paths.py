def print_root_to_leaf_paths(root):
    def construct_paths(node, path):
        if node is not None:
            path.append(node.data)  # Add current node to the path
            if node.left is None and node.right is None:  # If it's a leaf node
                print(" -> ".join(map(str, path)))  # Print the path
            else:
                construct_paths(node.left, path)  # Traverse left subtree
                construct_paths(node.right, path)  # Traverse right subtree
            path.pop()  # Remove the current node from the path

    construct_paths(root, [])

# Explanation:
# This function prints all root-to-leaf paths in a binary tree. 
# It uses a helper function `construct_paths` that recursively traverses the tree.
# When a leaf node is reached, it prints the current path from the root to that leaf.

# Big-O Analysis:
# The time complexity of this algorithm is O(N), where N is the number of nodes in the tree,
# because we visit each node exactly once. The space complexity is O(H), where H is the height of the tree,
# due to the recursion stack and the path storage. In the worst case (a skewed tree), H can be equal to N.