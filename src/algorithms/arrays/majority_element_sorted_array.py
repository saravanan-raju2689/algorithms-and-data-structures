def majority_element_sorted_array(arr):
    """
    Function to find the majority element in a sorted array.
    A majority element is an element that appears more than n/2 times in the array.

    Parameters:
    arr (list): A sorted list of integers.

    Returns:
    int: The majority element if it exists, otherwise -1.
    """
    n = len(arr)
    candidate = arr[n // 2]  # The middle element in a sorted array is a candidate

    # Check if the candidate is indeed the majority element
    count = arr.count(candidate)
    if count > n // 2:
        return candidate
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 1, 1, 2, 2, 3]
    print("Majority Element:", majority_element_sorted_array(arr))

# Big-O Analysis:
# Time Complexity: O(n) - We traverse the array to count occurrences of the candidate.
# Space Complexity: O(1) - We use a constant amount of space.