def rearrange_string(s, d):
    from collections import Counter
    import heapq

    # Count frequency of each character
    char_count = Counter(s)
    max_heap = []
    
    # Create a max heap based on character frequency
    for char, count in char_count.items():
        heapq.heappush(max_heap, (-count, char))

    result = []
    queue = []

    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)
        queue.append((count + 1, char))  # Decrease count and add to queue

        if len(queue) >= d:
            # If the queue is full, re-add the character back to the heap
            count, char = queue.pop(0)
            if count < 0:
                heapq.heappush(max_heap, (count, char))

    # Check if the rearrangement is possible
    if len(result) != len(s):
        return ""

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    s = "aaabc"
    d = 2
    print(rearrange_string(s, d))  # Output: "abaca" or similar valid arrangement

# Explanation:
# The function rearranges the string such that the same characters are at least 'd' distance apart.
# It uses a max heap to always place the most frequent characters first, ensuring that they are spaced out.

# Big-O Analysis:
# Time Complexity: O(n log k), where n is the length of the string and k is the number of unique characters.
# Space Complexity: O(k), for the heap and the queue used to store characters.