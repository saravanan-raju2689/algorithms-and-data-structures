def boolean_matrix_conditions(matrix):
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])
    row_zero = [False] * rows
    col_zero = [False] * cols

    # First pass: mark the rows and columns that need to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero[i] = True
                col_zero[j] = True

    # Second pass: zero out the marked rows
    for i in range(rows):
        if row_zero[i]:
            for j in range(cols):
                matrix[i][j] = 0

    # Third pass: zero out the marked columns
    for j in range(cols):
        if col_zero[j]:
            for i in range(rows):
                matrix[i][j] = 0

    return matrix