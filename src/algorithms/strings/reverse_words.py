def reverse_words(s):
    """
    Reverses the words in a given string.

    Parameters:
    s (str): The input string containing words to be reversed.

    Returns:
    str: A string with the words in reverse order.
    """
    # Split the string into words
    words = s.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list back into a string
    return ' '.join(reversed_words)

# Example usage
if __name__ == "__main__":
    input_string = "Hello World"
    output_string = reverse_words(input_string)
    print(output_string)  # Output: "World Hello"

"""
Big-O Analysis:
- Time Complexity: O(n), where n is the length of the input string. This is because we need to traverse the string to split it into words and then join it back.
- Space Complexity: O(n), as we are storing the words in a list and the final output string.
"""