def find_smallest_window(s, t):
    from collections import Counter

    if not t or not s:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)

    l, r = 0, 0
    formed = 0
    window_counts = {}
    min_length = float("inf")
    min_window = (0, 0)

    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]

            end = r - l + 1
            if end < min_length:
                min_length = end
                min_window = (l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1

        r += 1

    l, r = min_window
    return s[l:r + 1] if min_length != float("inf") else ""


# Explanation:
# The function finds the smallest substring in 's' that contains all characters of 't'.
# It uses a sliding window approach with two pointers and a hash map to count characters.

# Big-O Analysis:
# Time Complexity: O(N + M), where N is the length of s and M is the length of t.
# Space Complexity: O(M), for storing the character counts in the hash map.