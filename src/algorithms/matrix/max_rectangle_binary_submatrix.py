def max_rectangle_binary_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    max_area = 0
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * (cols + 1)

    for row in matrix:
        for col in range(cols):
            heights[col] = heights[col] + 1 if row[col] == 1 else 0

        stack = []
        for i in range(cols + 1):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area