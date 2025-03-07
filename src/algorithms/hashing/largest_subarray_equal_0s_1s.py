def largest_subarray_equal_0s_1s(arr):
    count_map = {}
    max_length = 0
    count = 0

    for i in range(len(arr)):
        count += 1 if arr[i] == 1 else -1

        if count == 0:
            max_length = i + 1

        if count in count_map:
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i

    return max_length