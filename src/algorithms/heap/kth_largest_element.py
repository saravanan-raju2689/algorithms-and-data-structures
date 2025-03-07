def kth_largest_element(stream, k):
    import heapq

    min_heap = []

    for num in stream:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0] if len(min_heap) == k else None