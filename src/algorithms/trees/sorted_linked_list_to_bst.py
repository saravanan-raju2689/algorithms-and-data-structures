def sorted_linked_list_to_bst(head):
    # Function to count the number of nodes in the linked list
    def count_nodes(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    # Function to convert sorted linked list to BST
    def convert_list_to_bst(left, right):
        nonlocal head
        if left > right:
            return None
        
        mid = (left + right) // 2
        
        # First, construct the left subtree
        left_child = convert_list_to_bst(left, mid - 1)
        
        # Now, head points to the middle node, make it the root
        root = TreeNode(head.val)
        root.left = left_child
        
        # Move to the next node in the linked list
        head = head.next
        
        # Construct the right subtree
        root.right = convert_list_to_bst(mid + 1, right)
        
        return root

    size = count_nodes(head)
    return convert_list_to_bst(0, size - 1)

# Explanation:
# This function converts a sorted linked list to a balanced binary search tree (BST).
# It first counts the number of nodes in the linked list, then recursively constructs
# the BST by finding the middle element of the linked list to ensure balance.

# Time Complexity: O(n)
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack).