def find_subarray_with_given_sum(arr, target_sum):
    """
    This function finds a subarray in the given array 'arr' that sums up to 'target_sum'.
    It uses a hash map to store the cumulative sum and its corresponding index.
    
    Parameters:
    arr (list): The input array of integers.
    target_sum (int): The target sum for which we need to find the subarray.
    
    Returns:
    tuple: The starting and ending indices of the subarray if found, otherwise (-1, -1).
    """
    cumulative_sum = 0
    sum_map = {}

    for i in range(len(arr)):
        cumulative_sum += arr[i]

        # Check if the current cumulative sum is equal to the target sum
        if cumulative_sum == target_sum:
            return (0, i)  # Subarray from index 0 to i

        # Check if there is a subarray (from some index to i) that sums to target_sum
        if (cumulative_sum - target_sum) in sum_map:
            return (sum_map[cumulative_sum - target_sum] + 1, i)

        # Store the cumulative sum with its index
        sum_map[cumulative_sum] = i

    return (-1, -1)  # No subarray found

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    target_sum = 12
    result = find_subarray_with_given_sum(arr, target_sum)
    if result != (-1, -1):
        print(f"Subarray found from index {result[0]} to {result[1]}")
    else:
        print("No subarray found")

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of elements in the array. 
# We traverse the array once and use a hash map for constant time lookups.
# Space Complexity: O(n), in the worst case, we may store all cumulative sums in the hash map.