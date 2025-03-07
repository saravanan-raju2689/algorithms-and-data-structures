# FILE: /algorithm-project/algorithm-project/src/explanations/trees.md

# Tree Algorithms Explanations and Big-O Analysis

## 1. Recursive Tree Traversals
This algorithm performs tree traversals (in-order, pre-order, post-order) recursively. 

- **Time Complexity**: O(n), where n is the number of nodes in the tree, as each node is visited once.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack.

## 2. Calculate Size of Tree
This algorithm calculates the total number of nodes in a binary tree.

- **Time Complexity**: O(n), where n is the number of nodes in the tree.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack.

## 3. Check Identical Trees
This algorithm checks if two binary trees are identical in structure and node values.

- **Time Complexity**: O(n), where n is the number of nodes in the smaller tree.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack.

## 4. Height of Tree
This algorithm calculates the height of a binary tree.

- **Time Complexity**: O(n), where n is the number of nodes in the tree.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack.

## 5. Delete Tree
This algorithm deletes a binary tree by deallocating all its nodes.

- **Time Complexity**: O(n), where n is the number of nodes in the tree.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack.

## 6. Convert to Mirror Tree
This algorithm converts a binary tree into its mirror tree.

- **Time Complexity**: O(n), where n is the number of nodes in the tree.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack.

## 7. Construct Tree from Traversals
This algorithm constructs a binary tree from given in-order and pre-order (or post-order) traversal sequences.

- **Time Complexity**: O(n), where n is the number of nodes in the tree.
- **Space Complexity**: O(n), for storing the indices of the nodes in a hash map.

## 8. Print Root to Leaf Paths
This algorithm prints all root-to-leaf paths in a binary tree.

- **Time Complexity**: O(n), where n is the number of nodes in the tree.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack.