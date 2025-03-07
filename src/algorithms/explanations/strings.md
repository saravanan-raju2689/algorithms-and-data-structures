# FILE: /algorithm-project/algorithm-project/src/explanations/strings.md

# String Algorithms Explanations and Big-O Analysis

## 1. Remove Duplicates from String
This algorithm iterates through the string and uses a set to track seen characters, constructing a new string without duplicates.
- **Time Complexity**: O(n), where n is the length of the string.
- **Space Complexity**: O(n) for the set.

## 2. Remove Characters
This algorithm removes characters from the first string that are present in the second string by using a set for fast lookups.
- **Time Complexity**: O(n + m), where n is the length of the first string and m is the length of the second string.
- **Space Complexity**: O(m) for the set of characters from the second string.

## 3. Check Rotations
This algorithm checks if one string is a rotation of another by concatenating the first string with itself and checking if the second string is a substring.
- **Time Complexity**: O(n), where n is the length of the string.
- **Space Complexity**: O(n) for the concatenated string.

## 4. Print Permutations
This algorithm generates all permutations of a string using recursion and backtracking.
- **Time Complexity**: O(n!), where n is the length of the string.
- **Space Complexity**: O(n) for the recursion stack.

## 5. Reverse Words
This algorithm splits the string into words, reverses the list of words, and joins them back into a single string.
- **Time Complexity**: O(n), where n is the length of the string.
- **Space Complexity**: O(n) for the list of words.

## 6. Find Smallest Window
This algorithm uses a sliding window approach to find the smallest substring containing all characters of another string.
- **Time Complexity**: O(n + m), where n is the length of the first string and m is the length of the second string.
- **Space Complexity**: O(m) for the character count.

## 7. Check Anagrams
This algorithm counts the frequency of characters in both strings and compares the counts.
- **Time Complexity**: O(n), where n is the length of the strings.
- **Space Complexity**: O(1) since the character set is fixed.

## 8. Custom Atoi
This algorithm converts a string to an integer, handling leading whitespace and optional signs.
- **Time Complexity**: O(n), where n is the length of the string.
- **Space Complexity**: O(1) since it uses a fixed amount of space.

## 9. Rearrange String
This algorithm rearranges a string so that no two adjacent characters are the same, using a max heap to track character frequencies.
- **Time Complexity**: O(n log k), where n is the length of the string and k is the number of unique characters.
- **Space Complexity**: O(k) for the heap.

## 10. Find Excel Column Name
This algorithm converts a given column number to its corresponding Excel column name using base-26 conversion.
- **Time Complexity**: O(log n), where n is the column number.
- **Space Complexity**: O(1) since it uses a fixed amount of space.