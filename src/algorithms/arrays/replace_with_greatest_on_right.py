def replace_with_greatest_on_right(arr):
    n = len(arr)
    if n == 0:
        return arr

    # Initialize the greatest element on the right
    greatest_on_right = arr[-1]

    # Traverse the array from the second last element to the first
    for i in range(n - 2, -1, -1):
        # Store the current element
        current = arr[i]
        # Replace the current element with the greatest on the right
        arr[i] = greatest_on_right
        # Update the greatest on the right if the current element is greater
        if current > greatest_on_right:
            greatest_on_right = current

    return arr

# Example usage
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print("Original array:", arr)
    print("Array after replacement:", replace_with_greatest_on_right(arr))

"""
Explanation:
The algorithm iterates through the array from right to left, keeping track of the greatest element encountered so far. For each element, it replaces it with the greatest element on its right. This is done in a single pass through the array.

Big-O Analysis:
Time Complexity: O(n), where n is the number of elements in the array. We traverse the array once.
Space Complexity: O(1), as we are using a constant amount of extra space.
"""