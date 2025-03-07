def sort_k_sorted_array(arr, k):
    from heapq import heappop, heappush

    if not arr:
        return arr

    min_heap = []
    result = []

    # Build a min heap of the first k+1 elements
    for i in range(min(k + 1, len(arr))):
        heappush(min_heap, arr[i])

    # One by one, extract the minimum element from the heap and add it to the result
    for i in range(k + 1, len(arr)):
        result.append(heappop(min_heap))
        heappush(min_heap, arr[i])

    # Extract the remaining elements from the heap
    while min_heap:
        result.append(heappop(min_heap))

    return result