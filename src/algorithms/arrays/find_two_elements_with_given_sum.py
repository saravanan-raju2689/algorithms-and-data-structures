def find_two_elements_with_given_sum(arr, target_sum):
    """
    This function finds two elements in the array that sum up to the given target_sum.
    
    Parameters:
    arr (list): The input array of integers.
    target_sum (int): The target sum to find in the array.
    
    Returns:
    tuple: A tuple containing the two elements that sum up to target_sum, or None if no such elements exist.
    """
    seen = {}
    for number in arr:
        complement = target_sum - number
        if complement in seen:
            return (complement, number)
        seen[number] = True
    return None

# Example usage:
# arr = [10, 15, 3, 7]
# target_sum = 17
# result = find_two_elements_with_given_sum(arr, target_sum)
# print(result)  # Output: (10, 7)

"""
Explanation:
The algorithm uses a hash map (dictionary) to store the elements of the array as we iterate through it. For each element, we calculate its complement (the value that, when added to the current element, equals the target sum). If the complement is found in the hash map, we return the pair.

Big-O Analysis:
- Time Complexity: O(n), where n is the number of elements in the array. We traverse the array once.
- Space Complexity: O(n), as we may store all elements in the hash map in the worst case.
"""