# FILE: /algorithm-project/algorithm-project/src/arrays/segregate_0s_1s.py

def segregate_0s_1s(arr):
    """
    This function takes an array of 0s and 1s and segregates them so that all 0s come before all 1s.
    
    Parameters:
    arr (list): A list containing only 0s and 1s.

    Returns:
    list: The input list with all 0s on the left and all 1s on the right.
    """
    zero_index = 0  # Pointer for the position of 0s

    for i in range(len(arr)):
        if arr[i] == 0:
            # Swap the elements
            arr[zero_index], arr[i] = arr[i], arr[zero_index]
            zero_index += 1

    return arr

# Example usage
if __name__ == "__main__":
    sample_array = [0, 1, 0, 1, 1, 0, 0, 1]
    print("Original array:", sample_array)
    segregated_array = segregate_0s_1s(sample_array)
    print("Segregated array:", segregated_array)

"""
Big-O Analysis:
- Time Complexity: O(n), where n is the number of elements in the array. We traverse the array once.
- Space Complexity: O(1), as we are using a constant amount of space for the pointers.
"""