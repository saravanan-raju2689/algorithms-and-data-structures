class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.prev = None
        self.next = None

def binary_tree_to_doubly_linked_list(root):
    if not root:
        return None

    # Initialize the previous node and head of the doubly linked list
    prev = None
    head = None

    def convert(node):
        nonlocal prev, head

        if not node:
            return

        # Convert the left subtree
        convert(node.left)

        # Process the current node
        if prev is None:
            head = node  # This is the first node
        else:
            node.prev = prev
            prev.next = node

        prev = node  # Update the previous node

        # Convert the right subtree
        convert(node.right)

    convert(root)
    return head

# Example usage:
# Construct a binary tree
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# Convert to doubly linked list
head = binary_tree_to_doubly_linked_list(root)

# Print the doubly linked list
current = head
while current:
    print(current.data, end=" <-> ")
    current = current.next

# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the tree due to recursion stack.