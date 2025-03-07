def majority_element(arr):
    """
    Function to find the majority element in an array.
    A majority element is an element that appears more than n/2 times in the array.
    
    Parameters:
    arr (list): The input array.

    Returns:
    int: The majority element if it exists, otherwise -1.
    """
    count = 0
    candidate = None

    # Phase 1: Find a candidate for majority element
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Phase 2: Verify if the candidate is actually the majority element
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    else:
        return -1

# Example usage
if __name__ == "__main__":
    arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print("Majority Element:", majority_element(arr))

"""
Big-O Analysis:
- Time Complexity: O(n), where n is the number of elements in the array. We traverse the array twice: once to find the candidate and once to verify it.
- Space Complexity: O(1), as we are using only a constant amount of space for variables.
"""