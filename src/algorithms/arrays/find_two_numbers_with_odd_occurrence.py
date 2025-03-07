def find_two_numbers_with_odd_occurrence(arr):
    # Initialize variables to store the two numbers
    x = 0
    y = 0
    # Step 1: XOR all elements in the array
    xor_sum = 0
    for num in arr:
        xor_sum ^= num
    
    # Step 2: Find a set bit in the xor_sum (rightmost set bit)
    set_bit = xor_sum & -xor_sum
    
    # Step 3: Divide elements into two groups and XOR them
    for num in arr:
        if num & set_bit:
            x ^= num  # Group with the set bit
        else:
            y ^= num  # Group without the set bit
    
    return x, y

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 1, 3, 5, 5]
    result = find_two_numbers_with_odd_occurrence(arr)
    print("The two numbers with odd occurrences are:", result)

# Explanation:
# This algorithm uses the properties of XOR to find two numbers that occur an odd number of times in an array.
# The first step is to XOR all the elements, which will give us the XOR of the two odd occurring numbers.
# Then, we find a set bit in the result to divide the numbers into two groups.
# Finally, we XOR the numbers in each group to get the two odd occurring numbers.

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the number of elements in the array.
# The space complexity is O(1) since we are using a constant amount of extra space.