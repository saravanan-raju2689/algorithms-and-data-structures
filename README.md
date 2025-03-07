# Algorithms and Data Structures Project

This project implements various algorithms and data structures in Python. The implementation is organized into different categories, including graph algorithms, matrix operations, queue and heap implementations, hashing techniques, and binary search tree operations.
## Table of Contents

- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project includes implementations of common algorithms and data structures, which are useful for solving various computational problems. The algorithms are categorized as follows:

- **Arrays**: Includes algorithms for finding elements, merging arrays, rotating arrays, and more.
- **Strings**: Contains algorithms for manipulating strings, such as removing duplicates, checking anagrams, and finding permutations.
- **Linked Lists**: Implements various linked list operations, including insertion, deletion, and reversal.
- **Trees**: Features algorithms for tree traversal, size calculation, and tree construction.

## Setup Instructions

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd algorithm-project
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Examples

Each algorithm can be executed by running the corresponding Python file in the `src` directory. For example, to find two elements with a given sum, run:
```
python src/arrays/find_two_elements_with_given_sum.py
```

Refer to the individual algorithm files for specific usage instructions and examples.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional algorithms, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

```
algorithms-and-data-structures
├── src
│   ├── algorithms
│   |   ├── arrays
│   |   ├── strings
│   |   ├── linked_list
│   |   ├── trees
│   |   ├── stack
│   │   ├── graph
│   │   │   ├── prim.py
│   │   │   ├── dijkstra.py
│   │   │   ├── bellman_ford.py
│   │   │   ├── transitive_closure.py
│   │   │   ├── topological_sort.py
│   │   │   ├── shortest_path_dag.py
│   │   │   ├── strongly_connected_components.py
│   │   │   ├── connectivity.py
│   │   │   ├── cycle_detection.py
│   │   │   ├── bfs_applications.py
│   │   ├── matrix
│   │   │   ├── max_square_submatrix.py
│   │   │   ├── rotate_image.py
│   │   │   ├── search_sorted_matrix.py
│   │   │   ├── spiral_print.py
│   │   │   ├── boolean_matrix.py
│   │   │   ├── min_cost_path.py
│   │   │   ├── count_islands.py
│   │   │   ├── max_sum_rectangle.py
│   │   │   ├── rotate_matrix_clockwise.py
│   │   │   ├── boolean_matrix_conditions.py
│   │   │   ├── max_rectangle_binary_submatrix.py
│   │   ├── queue
│   │   │   ├── level_order_traversal.py
│   │   │   ├── spiral_level_order_traversal.py
│   │   │   ├── queue_using_stacks.py
│   │   │   ├── stack_using_queues.py
│   │   │   ├── circular_tour.py
│   │   ├── heap
│   │   │   ├── k_largest_elements.py
│   │   │   ├── heap_applications.py
│   │   │   ├── build_heap.py
│   │   │   ├── median_in_stream.py
│   │   │   ├── sort_k_sorted_array.py
│   │   │   ├── merge_k_sorted_arrays.py
│   │   │   ├── sorted_order_from_matrix.py
│   │   │   ├── kth_smallest_element.py
│   │   │   ├── kth_largest_element.py
│   │   │   ├── heap_vs_bst.py
│   │   ├── hashing
│   │   │   ├── pair_sum.py
│   │   │   ├── vertical_sum.py
│   │   │   ├── largest_subarray_equal_0s_1s.py
│   │   │   ├── subarray_with_zero_sum.py
│   │   │   ├── special_data_structure.py
│   │   ├── bst
│   │   │   ├── find_min_element.py
│   │   │   ├── check_bst.py
│   │   │   ├── inorder_successor.py
│   │   │   ├── kth_smallest_element_bst.py
│   │   │   ├── sorted_list_to_bst.py
│   │   │   ├── construct_bst_preorder.py
├── requirements.txt
└── README.md
```

## Algorithms and Data Structures Included

### Trees

- **Lowest Common Ancestor in BST**: Finds the lowest common ancestor in a Binary Search Tree (BST). Time Complexity: O(h).
- **Level Order Traversal**: Implements level order traversal of a binary tree using a queue. Time Complexity: O(n).
- **Count Leaf Nodes**: Counts the number of leaf nodes in a binary tree. Time Complexity: O(n).
- **Spiral Level Order Traversal**: Implements spiral level order traversal of a binary tree. Time Complexity: O(n).
- **Diameter of Tree**: Calculates the diameter of a binary tree. Time Complexity: O(n).
- **Inorder Traversal Without Recursion**: Implements inorder traversal of a binary tree without recursion. Time Complexity: O(n).
- **Root to Leaf Path Sum**: Checks if there is a root-to-leaf path with a given sum. Time Complexity: O(n).
- **Construct Tree from Inorder and Preorder**: Constructs a binary tree from its inorder and preorder traversals. Time Complexity: O(n).
- **Nodes at K Distance**: Prints all nodes at a distance k from the root. Time Complexity: O(n).
- **Subtree Check**: Checks if one binary tree is a subtree of another. Time Complexity: O(n*m).
- **Inorder Successor**: Finds the inorder successor for all nodes in a BST. Time Complexity: O(n).
- **Vertical Sum**: Calculates the vertical sum in a binary tree. Time Complexity: O(n).
- **Maximum Sum Root to Leaf**: Finds the maximum sum from root to leaf. Time Complexity: O(n).
- **Complete Binary Tree Check**: Checks if a binary tree is complete. Time Complexity: O(n).
- **Iterative Preorder Traversal**: Implements iterative preorder traversal of a binary tree. Time Complexity: O(n).
- **Iterative Postorder Traversal**: Implements iterative postorder traversal of a binary tree. Time Complexity: O(n).
- **Reverse Level Order Traversal**: Implements reverse level order traversal of a binary tree. Time Complexity: O(n).
- **Binary Tree to Doubly Linked List**: Converts a binary tree to a doubly linked list. Time Complexity: O(n).
- **Height of Tree Iterative**: Finds the height of a binary tree iteratively. Time Complexity: O(n).
- **Left View of Binary Tree**: Prints the left view of a binary tree. Time Complexity: O(n).
- **Lowest Common Ancestor in Binary Tree**: Finds the lowest common ancestor in a binary tree. Time Complexity: O(n).
- **Nodes at K Distance from Given Node**: Prints all nodes at a distance k from a given node. Time Complexity: O(n).
- **Right View of Binary Tree**: Prints the right view of a binary tree. Time Complexity: O(n).
- **Subtree Check for Binary Trees**: Checks if one binary tree is a subtree of another binary tree. Time Complexity: O(n*m).
- **Nodes Between Levels**: Prints nodes between two given levels in a binary tree. Time Complexity: O(n).
- **Minimum Value Node in BST**: Finds the node with the minimum value in a BST. Time Complexity: O(h).
- **BST Check**: Checks if a binary tree is a BST. Time Complexity: O(n).
- **Kth Smallest Element in BST**: Finds the kth smallest element in a BST. Time Complexity: O(h + k).
- **Sorted Linked List to Balanced BST**: Converts a sorted linked list to a balanced BST. Time Complexity: O(n).
- **Kth Largest Element in BST**: Finds the kth largest element in a BST. Time Complexity: O(h + k).
- **Kth Smallest Element in BST using O(1) Space**: Finds the kth smallest element in a BST using O(1) space. Time Complexity: O(h + k).

### Stack

- **Queue Using Stack**: Implements a queue using stacks. Time Complexity: O(1) for enqueue, O(n) for dequeue.
- **Balanced Parentheses**: Checks for balanced parentheses in an expression. Time Complexity: O(n).
- **Reverse String Using Recursion**: Reverses a string using recursion. Time Complexity: O(n).
- **Special Stack**: Implements a special stack that supports additional operations. Time Complexity: O(1) for push and pop.
- **Stack Using Queues**: Implements a stack using queues. Time Complexity: O(1) for push, O(n) for pop.
- **Expression Evaluation**: Evaluates expressions using stacks. Time Complexity: O(n).

### Graph

- **MST Applications**: Discusses applications of Minimum Spanning Trees (MST).
- **DFS Applications**: Discusses applications of Depth-First Search (DFS).
- **DFS**: Implements Depth-First Search (DFS) for graph traversal. Time Complexity: O(V + E).
- **BFS**: Implements Breadth-First Search (BFS) for graph traversal. Time Complexity: O(V + E).
- **Detect Cycle in Directed Graph**: Detects cycles in a directed graph. Time Complexity: O(V + E).
- **Path Between Vertices**: Finds if there is a path between two vertices in a directed graph. Time Complexity: O(V + E).
- **Floyd-Warshall Algorithm**: Implements the Floyd-Warshall algorithm for finding shortest paths. Time Complexity: O(V^3).
- **Detect Cycle in Undirected Graph**: Detects cycles in an undirected graph. Time Complexity: O(V + E).
- **Kruskal's Algorithm**: Implements Kruskal's algorithm for finding the Minimum Spanning Tree. Time Complexity: O(E log E).
- **Graph Representations**: Discusses various representations of graphs.
- Prim's Algorithm
- Dijkstra's Algorithm
- Bellman-Ford Algorithm
- Transitive Closure
- Topological Sorting
- Shortest Path in Directed Acyclic Graph
- Strongly Connected Components
- Connectivity Check
- Cycle Detection
- BFS Applications

### Matrix Operations
- Maximum Size Square Submatrix with All 1s
- Image Rotation
- Search in Sorted Matrix
- Spiral Matrix Printing
- Boolean Matrix Questions
- Minimum Cost Path
- Island Counting
- Maximum Sum Rectangle in a 2D Matrix
- Clockwise Matrix Rotation
- Boolean Matrix Row and Column Conditions
- Maximum Size Rectangle Binary Submatrix with All 1s

### Queue Implementations
- Level Order Traversal
- Spiral Level Order Traversal
- Queue Implementation Using Stacks
- Stack Implementation Using Queues
- Circular Tour Problem

### Heap Operations
- K Largest Elements in an Array
- Heap Applications
- Heap Construction
- Median in a Stream
- K Sorted Array Sorting
- Merging K Sorted Arrays
- Sorted Order Printing from Sorted Matrix
- Kth Smallest Element in an Unsorted Array
- Kth Largest Element in a Stream
- Heap vs BST for Priority Queues

### Hashing Techniques
- Pair Sum Checking
- Vertical Sum in Binary Tree
- Largest Subarray with Equal Number of 0s and 1s
- Subarray with Zero Sum Checking
- Special Data Structure

### Binary Search Tree Operations
- Finding Minimum Element
- Checking if a Binary Tree is a BST
- Inorder Successor
- Kth Smallest Element Using Order Statistics
- Constructing BST from Preorder Traversal

## Requirements

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

Each algorithm and data structure is implemented in its respective file. You can import and use them as needed in your Python projects.