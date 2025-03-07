def max_sum_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    max_sum = float('-inf')
    rows, cols = len(matrix), len(matrix[0])

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            current_sum = 0
            current_max = float('-inf')
            for value in temp:
                current_sum += value
                current_max = max(current_max, current_sum)
                if current_sum < 0:
                    current_sum = 0

            max_sum = max(max_sum, current_max)

    return max_sum