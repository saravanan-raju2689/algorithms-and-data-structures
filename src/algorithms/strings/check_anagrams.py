def check_anagrams(str1, str2):
    """
    Check if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    bool: True if str1 and str2 are anagrams, False otherwise.
    """
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths are not the same, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Count characters in both strings
    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False

    return True

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the length of the strings.
# This is because we traverse each string once to count the characters.
# The space complexity is O(1) since the character count will not exceed the number of unique characters (constant space).