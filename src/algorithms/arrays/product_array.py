def product_array(arr):
    n = len(arr)
    if n == 0:
        return []

    # Initialize the output array
    output = [1] * n

    # Calculate the product of elements to the left of each index
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= arr[i]

    # Calculate the product of elements to the right of each index
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= arr[i]

    return output

# Explanation:
# The function calculates the product of all elements in the array except the current one.
# It does this by first calculating the product of all elements to the left of each index,
# and then multiplying it by the product of all elements to the right of each index.

# Big-O Analysis:
# Time Complexity: O(n) - We traverse the array twice.
# Space Complexity: O(1) - The output array is the only additional space used, which is required for the result.