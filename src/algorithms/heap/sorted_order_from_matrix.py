def sorted_order_from_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    min_heap = []

    for i in range(rows):
        min_heap.append((matrix[i][0], i, 0))

    import heapq
    heapq.heapify(min_heap)

    while min_heap:
        value, row, col = heapq.heappop(min_heap)
        result.append(value)

        if col + 1 < cols:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

    return result