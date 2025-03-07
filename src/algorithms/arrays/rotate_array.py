def rotate_array(arr, d):
    """
    Rotates the array to the left by d elements.
    
    Parameters:
    arr (list): The array to be rotated.
    d (int): The number of positions to rotate the array.
    
    Returns:
    list: The rotated array.
    """
    n = len(arr)
    d = d % n  # In case d is greater than n
    return arr[d:] + arr[:d]

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    rotated_array = rotate_array(arr, d)
    print("Rotated Array:", rotated_array)

# Explanation:
# The function rotates the array by slicing it into two parts: 
# the first part from index d to the end, and the second part from the start to index d.
# It then concatenates these two parts to form the rotated array.

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the number of elements in the array,
# because we are creating a new array that requires traversing all elements.
# The space complexity is also O(n) due to the new array created for the result.