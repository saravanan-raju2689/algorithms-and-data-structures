def find_number_occurring_odd_times(arr):
    """
    This function finds the number that occurs an odd number of times in an array.
    
    The approach uses the XOR operation, which has the property that:
    - a ^ a = 0 (XORing a number with itself results in 0)
    - a ^ 0 = a (XORing a number with 0 results in the number itself)
    
    By XORing all the elements in the array, the numbers that occur an even number of times will cancel each other out,
    leaving only the number that occurs an odd number of times.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The number that occurs an odd number of times.
    """
    result = 0
    for num in arr:
        result ^= num
    return result

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 3, 1, 1]
    print("The number occurring odd times is:", find_number_occurring_odd_times(arr))

# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space.