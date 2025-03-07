def find_common_elements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common_elements = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return common_elements

# Example usage
if __name__ == "__main__":
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    
    print("Common elements are:", find_common_elements(arr1, arr2, arr3))

# Explanation:
# The function `find_common_elements` takes three sorted arrays as input and finds the common elements among them.
# It uses a three-pointer technique to traverse the arrays simultaneously, which ensures that we only check each element once.

# Big-O Analysis:
# The time complexity of this algorithm is O(n), where n is the length of the longest array among the three.
# The space complexity is O(k), where k is the number of common elements found.