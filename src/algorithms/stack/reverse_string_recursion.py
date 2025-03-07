def reverse_string(s):
    """Recursively reverse a string."""
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Example usage
if __name__ == "__main__":
    input_string = "Hello, World!"
    reversed_string = reverse_string(input_string)
    print(f"Original String: {input_string}")
    print(f"Reversed String: {reversed_string}")

# Explanation:
# This function takes a string as input and reverses it using recursion.
# The base case is when the string is empty, in which case it returns the empty string.
# Otherwise, it returns the last character of the string concatenated with the result of
# the function called on the string excluding the last character.

# Time Complexity: O(n), where n is the length of the string. Each character is processed once.