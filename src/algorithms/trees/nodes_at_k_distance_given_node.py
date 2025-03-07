def nodes_at_k_distance_from_given_node(root, target, k):
    if root is None:
        return []

    # Helper function to find the target node and collect nodes at distance k
    def find_target_and_collect_nodes(node, target, k, result):
        if node is None:
            return -1
        
        if node == target:
            collect_nodes_at_distance_k(node, k, result)
            return 0
        
        left_distance = find_target_and_collect_nodes(node.left, target, k, result)
        if left_distance != -1:
            if left_distance + 1 == k:
                result.append(node.val)
            collect_nodes_at_distance_k(node.right, k - left_distance - 2, result)
            return left_distance + 1
        
        right_distance = find_target_and_collect_nodes(node.right, target, k, result)
        if right_distance != -1:
            if right_distance + 1 == k:
                result.append(node.val)
            collect_nodes_at_distance_k(node.left, k - right_distance - 2, result)
            return right_distance + 1
        
        return -1

    # Helper function to collect nodes at distance k from a given node
    def collect_nodes_at_distance_k(node, k, result):
        if node is None or k < 0:
            return
        if k == 0:
            result.append(node.val)
            return
        collect_nodes_at_distance_k(node.left, k - 1, result)
        collect_nodes_at_distance_k(node.right, k - 1, result)

    result = []
    find_target_and_collect_nodes(root, target, k, result)
    return result

# Explanation:
# This function finds all nodes at distance k from a given target node in a binary tree.
# It uses a helper function to traverse the tree and another helper function to collect nodes
# at the specified distance. The time complexity is O(n), where n is the number of nodes in the tree.