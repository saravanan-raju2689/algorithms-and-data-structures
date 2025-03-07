def is_balanced_parentheses(expression):
    stack = []
    parentheses = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if stack == [] or parentheses[char] != stack.pop():
                return False

    return stack == []

# Example usage
if __name__ == "__main__":
    expression = "{[()()]}"
    if is_balanced_parentheses(expression):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")

# Time Complexity: O(n), where n is the length of the expression.
# Space Complexity: O(n) in the worst case for the stack.