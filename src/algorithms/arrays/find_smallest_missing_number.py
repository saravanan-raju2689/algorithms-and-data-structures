def find_smallest_missing_number(arr):
    n = len(arr)
    
    # Step 1: Mark the presence of elements
    for i in range(n):
        # We only care about numbers in the range 1 to n
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            # Swap the elements to their correct positions
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

    # Step 2: Identify the smallest missing number
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1

# Example usage:
if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    print("The smallest missing number is:", find_smallest_missing_number(arr))

# Explanation:
# The algorithm first rearranges the array such that each number is placed at its corresponding index (i.e., number 1 at index 0, number 2 at index 1, etc.).
# After rearranging, the algorithm checks for the first index where the number does not match the index + 1, which indicates the smallest missing number.

# Big-O Analysis:
# The time complexity of this algorithm is O(n) because we traverse the array a constant number of times.
# The space complexity is O(1) since we are not using any additional data structures that grow with input size.