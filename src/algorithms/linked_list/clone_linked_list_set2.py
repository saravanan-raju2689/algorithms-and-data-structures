# FILE: /algorithm-project/algorithm-project/src/linked_list/clone_linked_list_set2.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def clone_linked_list(head):
    if not head:
        return None

    # Step 1: Create a copy of each node and insert it next to the original node
    current = head
    while current:
        new_node = Node(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Set the random pointers for the copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original and copied linked lists
    original = head
    copy_head = head.next
    copy_current = copy_head

    while original:
        original.next = original.next.next
        if copy_current.next:
            copy_current.next = copy_current.next.next
        original = original.next
        copy_current = copy_current.next if copy_current else None

    return copy_head

# Big-O Analysis:
# Time Complexity: O(n) - We traverse the list three times.
# Space Complexity: O(1) - We are using the existing nodes to create the clone without using extra space for a hash map.