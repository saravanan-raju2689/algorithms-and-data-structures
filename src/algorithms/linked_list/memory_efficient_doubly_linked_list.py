class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class MemoryEfficientDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def delete(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node = None

    def find(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

# Explanation:
# This implementation of a memory-efficient doubly linked list uses a Node class to represent each node.
# Each node contains data, a pointer to the previous node, and a pointer to the next node.
# The MemoryEfficientDoublyLinkedList class manages the list, allowing for appending, displaying, deleting, and finding nodes.

# Big-O Analysis:
# - Append: O(n) in the worst case, where n is the number of nodes in the list (if we need to traverse to the end).
# - Display: O(n), as we need to traverse the entire list.
# - Delete: O(1) if the node to be deleted is known; otherwise, O(n) to find the node.
# - Find: O(n), as we may need to traverse the entire list to find the node.