def boolean_matrix(matrix):
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])
    row_flag = [False] * rows
    col_flag = [False] * cols

    # First pass: mark the rows and columns that need to be set to 1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_flag[i] = True
                col_flag[j] = True

    # Second pass: update the matrix
    for i in range(rows):
        for j in range(cols):
            if row_flag[i] or col_flag[j]:
                matrix[i][j] = 1

    return matrix