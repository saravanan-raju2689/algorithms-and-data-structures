def print_permutations(s, prefix=""):
    """
    Prints all permutations of a given string.

    Args:
    s (str): The string to permute.
    prefix (str): The current prefix for the permutation.

    Returns:
    None
    """
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            # Recursive call with the remaining characters
            print_permutations(s[:i] + s[i+1:], prefix + s[i])

# Example usage
if __name__ == "__main__":
    input_string = "abc"
    print("Permutations of", input_string, ":")
    print_permutations(input_string)

"""
Explanation:
The function `print_permutations` generates all permutations of a given string `s`. It does this by recursively selecting each character in the string and appending it to a prefix until no characters are left.

Big-O Analysis:
The time complexity of generating all permutations of a string of length n is O(n!), as there are n! possible permutations. The space complexity is O(n) for the recursion stack.
"""