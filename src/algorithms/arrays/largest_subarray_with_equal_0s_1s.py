# FILE: /algorithm-project/algorithm-project/src/arrays/largest_subarray_with_equal_0s_1s.py

def largest_subarray_with_equal_0s_1s(arr):
    n = len(arr)
    max_length = 0
    sum_index_map = {}
    sum_so_far = 0

    for i in range(n):
        # Treat 0 as -1 to use the sum technique
        sum_so_far += 1 if arr[i] == 1 else -1

        if sum_so_far == 0:
            max_length = i + 1
        elif sum_so_far in sum_index_map:
            max_length = max(max_length, i - sum_index_map[sum_so_far])
        else:
            sum_index_map[sum_so_far] = i

    return max_length

# Explanation:
# The algorithm uses a hash map to store the first occurrence of each sum.
# It treats 0 as -1 to find the largest subarray with equal numbers of 0s and 1s.
# When the same sum occurs again, it indicates that the elements between the two indices
# have an equal number of 0s and 1s.

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the number of elements in the array.
# The space complexity is O(n) due to the hash map used to store the sum indices.