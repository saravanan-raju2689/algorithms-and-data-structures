def median_in_stream(stream):
    import heapq

    min_heap = []  # To store the larger half of the numbers
    max_heap = []  # To store the smaller half of the numbers

    medians = []

    for number in stream:
        # Add to max_heap (smaller half)
        heapq.heappush(max_heap, -number)

        # Ensure max_heap's largest is <= min_heap's smallest
        if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # Balance the heaps
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Calculate median
        if len(max_heap) > len(min_heap):
            medians.append(-max_heap[0])
        else:
            medians.append((-max_heap[0] + min_heap[0]) / 2)

    return medians