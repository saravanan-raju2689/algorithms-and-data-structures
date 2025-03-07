def k_largest_elements(arr, k):
    if k <= 0 or k > len(arr):
        return []

    # Using a min-heap to keep track of the k largest elements
    import heapq
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return sorted(min_heap, reverse=True)  # Return the k largest elements in descending order