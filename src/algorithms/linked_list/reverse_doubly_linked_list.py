# FILE: /algorithm-project/algorithm-project/src/linked_list/reverse_doubly_linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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

    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    
    print("Original list:")
    dll.print_list()
    
    dll.reverse()
    
    print("Reversed list:")
    dll.print_list()

"""
Explanation:
The above code defines a doubly linked list and implements a method to reverse it. The `reverse` method iterates through the list, swapping the `next` and `prev` pointers for each node. After the loop, it updates the head of the list to the last processed node.

Big-O Analysis:
- Time Complexity: O(n), where n is the number of nodes in the doubly linked list, as we traverse the list once.
- Space Complexity: O(1), as we are using a constant amount of space for pointers.
"""