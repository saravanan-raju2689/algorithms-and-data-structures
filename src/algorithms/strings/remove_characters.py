def remove_characters(str1, str2):
    """
    Remove characters from str1 that are present in str2.

    Parameters:
    str1 (str): The original string from which characters will be removed.
    str2 (str): The string containing characters to be removed from str1.

    Returns:
    str: A new string with characters from str2 removed from str1.
    """
    # Create a set of characters to remove for O(1) lookup
    chars_to_remove = set(str2)
    
    # Use a list comprehension to build the result string
    result = ''.join([char for char in str1 if char not in chars_to_remove])
    
    return result

# Example usage
if __name__ == "__main__":
    str1 = "hello world"
    str2 = "aeiou"
    print(remove_characters(str1, str2))  # Output: "hll wrld"

"""
Big-O Analysis:
- Time Complexity: O(n + m), where n is the length of str1 and m is the length of str2.
  - Creating the set of characters to remove takes O(m).
  - Iterating through str1 to build the result takes O(n).
- Space Complexity: O(m) for the set of characters to remove.
"""