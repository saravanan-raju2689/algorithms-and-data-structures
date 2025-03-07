# Linked List Algorithms Explanations and Big-O Analysis

## 1. Get Nth Node in a Linked List
This algorithm retrieves the Nth node from the start of a linked list. It iterates through the list until it reaches the desired node.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 2. Delete a Node Given a Pointer to It
This algorithm deletes a node from a linked list given a pointer to that node. It copies the data from the next node to the current node and deletes the next node.

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

## 3. Print Middle of a Linked List
This algorithm finds and prints the middle node of a linked list using the two-pointer technique (slow and fast pointers).

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 4. Find Nth Node from the End
This algorithm finds the Nth node from the end of a linked list using two pointers. The first pointer advances N nodes ahead, and then both pointers move together until the first pointer reaches the end.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 5. Delete Linked List
This algorithm deletes an entire linked list by iterating through the list and freeing each node.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 6. Reverse Linked List
This algorithm reverses a linked list by changing the next pointers of each node.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 7. Detect Loop in a Linked List
This algorithm detects a loop in a linked list using Floyd’s Cycle Detection algorithm (tortoise and hare).

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 8. Check if a Singly Linked List is a Palindrome
This algorithm checks if a linked list is a palindrome by reversing the second half of the list and comparing it with the first half.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 9. Clone a Linked List with Next and Random Pointer
This algorithm clones a linked list where each node has a next and a random pointer. It uses a hash map to store the mapping of original nodes to their clones.

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

## 10. Memory Efficient Doubly Linked List
This algorithm implements a memory-efficient doubly linked list using a single pointer for each node.

**Time Complexity:** O(1) for insertion and deletion  
**Space Complexity:** O(N)

## 11. Insert in Sorted Linked List
This algorithm inserts a new node into a sorted linked list while maintaining the order.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 12. Get Intersection Point of Two Linked Lists
This algorithm finds the intersection point of two linked lists by calculating their lengths and aligning them before traversing.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 13. Print Reverse of a Linked List
This algorithm prints the elements of a linked list in reverse order using recursion.

**Time Complexity:** O(N)  
**Space Complexity:** O(N) due to recursion stack

## 14. Remove Duplicates from Sorted Linked List
This algorithm removes duplicates from a sorted linked list by comparing adjacent nodes.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 15. Remove Duplicates from Unsorted Linked List
This algorithm removes duplicates from an unsorted linked list using a hash set to track seen values.

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

## 16. Reverse Doubly Linked List
This algorithm reverses a doubly linked list by swapping the next and previous pointers.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 17. Merge Two Sorted Linked Lists
This algorithm merges two sorted linked lists into a single sorted linked list.

**Time Complexity:** O(N + M) where N and M are the lengths of the two lists  
**Space Complexity:** O(1)

## 18. Merge Sort for Linked Lists
This algorithm sorts a linked list using the merge sort algorithm.

**Time Complexity:** O(N log N)  
**Space Complexity:** O(log N) due to recursion stack

## 19. Reverse a Linked List in Groups of Given Size
This algorithm reverses nodes in groups of a specified size.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 20. Linked List vs Array
This section compares linked lists and arrays in terms of memory usage, access time, and insertion/deletion efficiency.

**Time Complexity:** Varies based on operation  
**Space Complexity:** Varies based on structure

## 21. Sorted Insert for Circular Linked List
This algorithm inserts a node into a circular linked list while maintaining the sorted order.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 22. Detect and Remove Loop in a Linked List
This algorithm detects a loop in a linked list and removes it if found.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 23. Add Two Numbers Represented by Linked Lists
This algorithm adds two numbers represented by linked lists and returns the sum as a linked list.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

## 24. Clone a Linked List with Next and Random Pointer | Set 2
This algorithm is a variation of the first cloning algorithm, using a different approach for cloning.

**Time Complexity:** O(N)  
**Space Complexity:** O(N)