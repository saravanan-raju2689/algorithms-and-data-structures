def find_excel_column_name(column_number):
    """
    Given a column number, return its corresponding Excel column name.
    
    Args:
    column_number (int): The column number (1-indexed).
    
    Returns:
    str: The corresponding Excel column name.
    """
    column_name = ""
    while column_number > 0:
        # Find the remainder when divided by 26
        remainder = (column_number - 1) % 26
        # Convert remainder to corresponding character
        column_name = chr(remainder + ord('A')) + column_name
        # Update column_number for the next iteration
        column_number = (column_number - 1) // 26
    return column_name

# Example usage
if __name__ == "__main__":
    print(find_excel_column_name(1))    # Output: A
    print(find_excel_column_name(28))   # Output: AB
    print(find_excel_column_name(701))  # Output: ZY

"""
Explanation:
The algorithm converts a given column number to its corresponding Excel column name by repeatedly dividing the number by 26 and using the remainder to determine the character. The process continues until the column number is reduced to zero.

Big-O Analysis:
The time complexity of this algorithm is O(log n), where n is the column number. This is because we divide the column number by 26 in each iteration, leading to a logarithmic number of iterations. The space complexity is O(1) since we are using a fixed amount of space for variables. 
"""