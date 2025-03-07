def merge_k_sorted_arrays(arrays):
    import heapq

    min_heap = []
    for i, array in enumerate(arrays):
        if array:  # Check if the array is not empty
            heapq.heappush(min_heap, (array[0], i, 0))  # (value, array index, element index)

    merged_array = []
    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)
        merged_array.append(value)

        if element_index + 1 < len(arrays[array_index]):
            next_tuple = (arrays[array_index][element_index + 1], array_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged_array