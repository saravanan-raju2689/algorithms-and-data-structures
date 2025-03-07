def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]

    return water_trapped

# Explanation:
# The algorithm uses a two-pointer approach to calculate the amount of water that can be trapped.
# It maintains two pointers, one at the beginning (left) and one at the end (right) of the height array.
# The left_max and right_max variables keep track of the maximum heights encountered from both ends.
# Water is trapped when the current height is less than the maximum height from either side.

# Big-O Analysis:
# Time Complexity: O(n), where n is the number of elements in the height array. 
# We traverse the array once with the two pointers.
# Space Complexity: O(1), as we are using only a constant amount of extra space.