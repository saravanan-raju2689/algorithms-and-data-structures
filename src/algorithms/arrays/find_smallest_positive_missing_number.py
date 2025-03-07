def find_smallest_positive_missing_number(arr):
    n = len(arr)
    
    # Step 1: Mark numbers (num < 1 or num > n) as n+1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = n + 1

    # Step 2: Use the index as a hash to mark the presence of numbers
    for i in range(n):
        num = abs(arr[i])
        if 1 <= num <= n:
            arr[num - 1] = -abs(arr[num - 1])

    # Step 3: Find the first index which is positive
    for i in range(n):
        if arr[i] > 0:
            return i + 1

    # If all indices are marked, the smallest missing positive is n + 1
    return n + 1

# Example usage
if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    print("The smallest positive missing number is:", find_smallest_positive_missing_number(arr))

# Explanation:
# The algorithm works by first marking all numbers that are out of the range [1, n] as n + 1.
# Then, it uses the indices of the array to mark the presence of numbers in the range [1, n].
# Finally, it checks for the first index that remains positive, which indicates the smallest missing positive number.

# Big-O Analysis:
# The time complexity of this algorithm is O(n) because we traverse the array a constant number of times.
# The space complexity is O(1) since we are modifying the input array in place without using any extra space.