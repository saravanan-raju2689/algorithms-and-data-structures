def find_two_repeating_elements(arr):
    n = len(arr) - 2  # Since there are two repeating elements
    repeating = []
    
    # Using a set to track seen elements
    seen = set()
    
    for num in arr:
        if num in seen:
            repeating.append(num)
        else:
            seen.add(num)
    
    return repeating

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 1, 4]
    print("Repeating elements are:", find_two_repeating_elements(arr))

"""
Explanation:
The algorithm uses a set to keep track of the elements that have been seen as we iterate through the array. When we encounter an element that is already in the set, we add it to the list of repeating elements. This approach ensures that we only traverse the array once.

Big-O Analysis:
- Time Complexity: O(n), where n is the number of elements in the array. We traverse the array once.
- Space Complexity: O(n), in the worst case, we may store all elements in the set.
"""