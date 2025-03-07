def find_max_j_i(arr):
    """
    This function finds the maximum value of j - i such that arr[j] > arr[i].
    
    Parameters:
    arr (list): The input array of integers.

    Returns:
    int: The maximum value of j - i, or -1 if no such pair exists.
    """
    n = len(arr)
    max_diff = -1
    left_min = arr[0]

    for j in range(1, n):
        if arr[j] < left_min:
            left_min = arr[j]
        else:
            max_diff = max(max_diff, j - arr.index(left_min))

    return max_diff

# Example usage:
# arr = [1, 2, 3, 4, 5]
# print(find_max_j_i(arr))  # Output: 4 (j=4, i=0)

# Time Complexity: O(n^2) in the worst case, as we may need to search for the index of left_min for each j.
# Space Complexity: O(1) as we are using a constant amount of space.