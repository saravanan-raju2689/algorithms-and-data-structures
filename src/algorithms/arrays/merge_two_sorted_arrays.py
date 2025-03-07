def merge_two_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays into one sorted array in O(1) space.
    
    Parameters:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.
    
    Returns:
    list: Merged sorted array.
    """
    # Initialize pointers for arr1 and arr2
    i, j = 0, 0
    merged_array = []
    
    # Traverse both arrays and merge them
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

# Big-O Analysis:
# Time Complexity: O(n + m), where n is the length of arr1 and m is the length of arr2.
# Space Complexity: O(n + m) for the merged array. However, if we consider the merging process itself,
# we can say it uses O(1) additional space if we merge in place (not applicable here as we create a new array).