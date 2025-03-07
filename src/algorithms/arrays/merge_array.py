def merge_arrays(arr1, arr2):
    """
    Merges two sorted arrays into one sorted array.

    Parameters:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.

    Returns:
    list: Merged sorted array.
    """
    merged_array = []
    i, j = 0, 0

    # Traverse both arrays and insert smaller element into merged_array
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # If there are remaining elements in arr1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # If there are remaining elements in arr2
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

# Example usage
if __name__ == "__main__":
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    print("Merged Array:", merge_arrays(arr1, arr2))

"""
Explanation:
The merge_arrays function takes two sorted arrays as input and merges them into a single sorted array. It uses two pointers to traverse both arrays and appends the smaller element to the merged array. 

Big-O Analysis:
- Time Complexity: O(n + m), where n and m are the lengths of the two arrays. This is because we traverse both arrays once.
- Space Complexity: O(n + m) for the merged array.
"""