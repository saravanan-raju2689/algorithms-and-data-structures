# FILE: /algorithm-project/algorithm-project/src/linked_list/clone_linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def clone_linked_list(head):
    if not head:
        return None

    # Step 1: Create a copy of each node and insert it right next to the original node
    current = head
    while current:
        new_node = Node(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Assign random pointers for the copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original and cloned linked list
    original = head
    clone_head = head.next
    clone_current = clone_head

    while original:
        original.next = clone_current.next
        original = original.next
        if clone_current.next:
            clone_current.next = original.next
            clone_current = clone_current.next

    return clone_head

# Big-O Analysis:
# Time Complexity: O(N) - We traverse the list three times.
# Space Complexity: O(1) - We are using the original nodes to store the cloned nodes, so no extra space is used for the nodes themselves.