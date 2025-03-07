def kth_smallest_element(arr, k):
    if k < 1 or k > len(arr):
        return None

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect(low, high, k):
        if low < high:
            pivot_index = partition(low, high)
            if pivot_index == k - 1:
                return arr[pivot_index]
            elif pivot_index > k - 1:
                return quickselect(low, pivot_index - 1, k)
            else:
                return quickselect(pivot_index + 1, high, k)
        return arr[low]

    return quickselect(0, len(arr) - 1, k)