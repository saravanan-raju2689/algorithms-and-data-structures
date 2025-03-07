def evaluate_expression(expression):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def apply_operation(a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b

    values = []
    ops = []
    i = 0

    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        if expression[i].isdigit():
            val = 0
            while (i < len(expression) and expression[i].isdigit()):
                val = (val * 10) + int(expression[i])
                i += 1
            values.append(val)

        else:
            while (ops and precedence(ops[-1]) >= precedence(expression[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_operation(val1, val2, op))
            ops.append(expression[i])
            i += 1

    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_operation(val1, val2, op))

    return values[-1]

# Explanation:
# This function evaluates a mathematical expression given in string format.
# It uses two stacks: one for values and another for operators.
# The time complexity of this algorithm is O(n), where n is the length of the expression.