def my_atoi(s: str) -> int:
    """
    Implement a custom atoi function that converts a string to an integer.
    
    Args:
    s (str): The input string to convert.
    
    Returns:
    int: The converted integer value.
    """
    s = s.strip()  # Remove leading and trailing whitespace
    if not s:
        return 0

    sign = 1
    index = 0
    result = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Check for sign
    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1

    # Convert characters to integer
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        
        # Check for overflow and underflow
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        index += 1

    return sign * result

# Big-O Analysis:
# Time Complexity: O(n), where n is the length of the input string. We traverse the string once.
# Space Complexity: O(1), as we are using a constant amount of space for variables.