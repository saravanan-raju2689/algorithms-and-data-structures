def nuts_and_bolts_problem(nuts, bolts):
    """
    This function solves the nuts and bolts problem, where we have two arrays: 
    one containing nuts and the other containing bolts. The goal is to match 
    each nut with its corresponding bolt.

    The approach uses a modified quicksort algorithm to sort both arrays. 
    We use the nuts to partition the bolts and vice versa, ensuring that 
    each nut matches with its corresponding bolt.

    Time Complexity: O(n log n) on average, O(n^2) in the worst case due to 
    the quicksort partitioning.
    Space Complexity: O(log n) for the recursive stack space.
    """
    def match_pairs(nuts, bolts, low, high):
        if low < high:
            # Choose the last bolt as the pivot
            pivot = bolts[high]
            # Partition nuts based on the pivot
            i = low
            for j in range(low, high):
                if nuts[j] < pivot:
                    nuts[i], nuts[j] = nuts[j], nuts[i]
                    i += 1
                elif nuts[j] == pivot:
                    nuts[j], nuts[high] = nuts[high], nuts[j]
                    j -= 1
            nuts[i], nuts[high] = nuts[high], nuts[i]

            # Now partition bolts based on the nut at index i
            pivot = nuts[i]
            j = low
            for j in range(low, high):
                if bolts[j] < pivot:
                    bolts[i], bolts[j] = bolts[j], bolts[i]
                    i += 1
                elif bolts[j] == pivot:
                    bolts[j], bolts[high] = bolts[high], bolts[j]
                    j -= 1
            bolts[i], bolts[high] = bolts[high], bolts[i]

            # Recursively sort the nuts and bolts
            match_pairs(nuts, bolts, low, i - 1)
            match_pairs(nuts, bolts, i + 1, high)

    match_pairs(nuts, bolts, 0, len(nuts) - 1)

# Example usage
nuts = ['@', '#', '$', '%', '^']
bolts = ['$', '%', '^', '@', '#']
nuts_and_bolts_problem(nuts, bolts)
print("Matched Nuts and Bolts:")
print("Nuts:", nuts)
print("Bolts:", bolts)