# FILE: /algorithm-project/algorithm-project/src/linked_list/linked_list_vs_array.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def compare_linked_list_and_array():
    # Linked List vs Array
    print("Linked List vs Array")
    print("1. Memory Usage:")
    print("   - Arrays use contiguous memory, which can lead to memory wastage if the size is not optimal.")
    print("   - Linked Lists use non-contiguous memory, which can lead to overhead due to pointers.")
    
    print("2. Access Time:")
    print("   - Arrays provide O(1) access time for elements.")
    print("   - Linked Lists provide O(n) access time as traversal is required.")
    
    print("3. Insertion/Deletion:")
    print("   - Arrays require O(n) time for insertion/deletion as elements need to be shifted.")
    print("   - Linked Lists provide O(1) time for insertion/deletion if the pointer to the node is known.")
    
    print("4. Size:")
    print("   - Arrays have a fixed size, which can lead to overflow or wastage.")
    print("   - Linked Lists can grow and shrink dynamically.")

if __name__ == "__main__":
    # Example usage
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()
    
    compare_linked_list_and_array()

# Big-O Analysis:
# - Memory Usage: O(n) for both, but arrays may waste space.
# - Access Time: O(1) for arrays, O(n) for linked lists.
# - Insertion/Deletion: O(n) for arrays, O(1) for linked lists (if node is known).
# - Size: Dynamic for linked lists, fixed for arrays.