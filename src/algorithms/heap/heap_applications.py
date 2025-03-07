def heap_applications():
    # Example application: Find the k largest elements in an array
    def k_largest_elements(arr, k):
        import heapq
        return heapq.nlargest(k, arr)

    # Example application: Merge k sorted arrays
    def merge_k_sorted_arrays(arrays):
        import heapq
        min_heap = []
        for i, array in enumerate(arrays):
            if array:
                heapq.heappush(min_heap, (array[0], i, 0))
        
        merged_array = []
        while min_heap:
            value, array_index, element_index = heapq.heappop(min_heap)
            merged_array.append(value)
            if element_index + 1 < len(arrays[array_index]):
                next_tuple = (arrays[array_index][element_index + 1], array_index, element_index + 1)
                heapq.heappush(min_heap, next_tuple)
        
        return merged_array

    # Example application: Find the median in a stream of integers
    class MedianFinder:
        def __init__(self):
            self.min_heap = []  # Stores the larger half
            self.max_heap = []  # Stores the smaller half

        def add_num(self, num):
            heapq.heappush(self.max_heap, -num)
            if self.max_heap and (-self.max_heap[0]) > (self.min_heap[0] if self.min_heap else float('inf')):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

            if len(self.max_heap) > len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            elif len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        def find_median(self):
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            return (-self.max_heap[0] + self.min_heap[0]) / 2

    # Example application: Sort a k sorted array
    def sort_k_sorted_array(arr, k):
        import heapq
        min_heap = []
        result = []
        
        for i in range(min(k + 1, len(arr))):
            heapq.heappush(min_heap, arr[i])
        
        for i in range(k + 1, len(arr)):
            result.append(heapq.heappop(min_heap))
            heapq.heappush(min_heap, arr[i])
        
        while min_heap:
            result.append(heapq.heappop(min_heap))
        
        return result

    return {
        "k_largest_elements": k_largest_elements,
        "merge_k_sorted_arrays": merge_k_sorted_arrays,
        "MedianFinder": MedianFinder,
        "sort_k_sorted_array": sort_k_sorted_array
    }