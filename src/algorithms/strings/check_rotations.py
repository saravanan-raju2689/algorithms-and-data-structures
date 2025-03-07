def check_rotations(str1, str2):
    """
    Check if str2 is a rotation of str1.
    
    A string str2 is a rotation of str1 if it can be obtained by moving some characters from the beginning of str1 to the end.
    
    Approach:
    1. Check if the lengths of str1 and str2 are equal. If not, return False.
    2. Concatenate str1 with itself (str1 + str1).
    3. Check if str2 is a substring of the concatenated string.
    
    Time Complexity: O(n), where n is the length of the strings.
    Space Complexity: O(n), for the concatenated string.
    """
    if len(str1) != len(str2):
        return False
    
    concatenated = str1 + str1
    return str2 in concatenated

# Example usage
if __name__ == "__main__":
    str1 = "abcde"
    str2 = "deabc"
    print(check_rotations(str1, str2))  # Output: True

    str3 = "abcde"
    str4 = "abced"
    print(check_rotations(str3, str4))  # Output: False