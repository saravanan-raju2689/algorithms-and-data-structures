# FILE: /algorithm-project/algorithm-project/src/explanations/arrays.md

# Arrays Algorithms Explanations and Big-O Analysis

## 1. Find Two Elements with Given Sum
This algorithm finds two elements in an array that sum up to a specified value. It uses a hash set to store the elements and checks if the complement (target - current element) exists in the set.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

## 2. Majority Element
This algorithm identifies the majority element (the element that appears more than n/2 times) in an array using the Boyer-Moore Voting Algorithm.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 3. Find Number Occurring Odd Number of Times
This algorithm uses the XOR operation to find the number that occurs an odd number of times in an array. The property of XOR is that it cancels out the even occurrences.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 4. Merge an Array of Size n into Another of Size m + n
This algorithm merges two sorted arrays into a single sorted array. It starts from the end of both arrays to avoid overwriting elements.

**Time Complexity:** O(m + n)  
**Space Complexity:** O(1)

## 5. Rotate an Array
This algorithm rotates an array to the right by k steps. It reverses the entire array, then reverses the first k elements and the remaining elements.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 6. Leaders in an Array
This algorithm finds all the leaders in an array (elements that are greater than all the elements to their right). It traverses the array from right to left.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 7. Majority Element in Sorted Array
This algorithm finds the majority element in a sorted array by checking the middle element and its frequency.

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

## 8. Segregate 0s and 1s in an Array
This algorithm segregates 0s and 1s in an array by using two pointers.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 9. Product Array
This algorithm calculates the product of all elements except the current one using two passes through the array.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 10. Find Two Repeating Elements
This algorithm finds two repeating elements in an array using a hash set to track seen elements.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

## 11. Find the Smallest Missing Number
This algorithm finds the smallest missing positive number in an unsorted array by rearranging the elements.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 12. Find Max j - i such that arr[j] > arr[i]
This algorithm finds the maximum difference j - i such that arr[j] > arr[i] by maintaining the minimum value seen so far.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 13. Find Subarray with Given Sum
This algorithm finds a subarray with a given sum using a hash map to store cumulative sums.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

## 14. Find the Smallest Positive Number Missing from an Unsorted Array
This algorithm finds the smallest positive number missing from an unsorted array by rearranging the elements.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 15. Find Two Numbers with Odd Occurrence
This algorithm finds two numbers that occur an odd number of times using XOR.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 16. Largest Subarray with Equal Number of 0s and 1s
This algorithm finds the largest subarray with an equal number of 0s and 1s by using a hash map to store the first occurrence of each cumulative sum.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

## 17. Replace Every Element with the Greatest on Right Side
This algorithm replaces every element with the greatest element on its right side by traversing the array from right to left.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 18. Stock Buy Sell to Maximize Profit
This algorithm finds the maximum profit from stock prices by tracking the minimum price seen so far.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 19. Find Common Elements in Three Sorted Arrays
This algorithm finds common elements in three sorted arrays using three pointers.

**Time Complexity:** O(n1 + n2 + n3)  
**Space Complexity:** O(1)

## 20. Nuts and Bolts Problem
This algorithm matches nuts and bolts using a comparison-based approach.

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)

## 21. Trapping Rain Water
This algorithm calculates the amount of trapped rainwater using two pointers.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## 22. Merge Two Sorted Arrays in O(1) Space
This algorithm merges two sorted arrays without using extra space by utilizing the end of the first array.

**Time Complexity:** O(m + n)  
**Space Complexity:** O(1)