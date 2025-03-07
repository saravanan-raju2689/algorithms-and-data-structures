def remove_duplicates(s):
    """
    Remove duplicates from a string while maintaining the order of characters.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: A new string with duplicates removed.
    """
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    input_string = "geeksforgeeks"
    output_string = remove_duplicates(input_string)
    print(f"Original String: {input_string}")
    print(f"String after removing duplicates: {output_string}")

# Big-O Analysis:
# Time Complexity: O(n), where n is the length of the input string. 
# We traverse the string once and perform constant time operations for each character.
# Space Complexity: O(min(n, m)), where n is the size of the input string and m is the size of the character set. 
# We use a set to store the characters, which in the worst case can be as large as the input string.