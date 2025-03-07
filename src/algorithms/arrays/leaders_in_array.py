def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[n - 1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)

    return leaders[::-1]  # Reverse the list to maintain original order


# Example usage:
if __name__ == "__main__":
    array = [16, 17, 4, 3, 5, 2]
    print("Leaders in the array are:", find_leaders(array))

"""
Explanation:
The algorithm finds leaders in an array, where a leader is an element that is greater than all the elements to its right. 
We start from the rightmost element and keep track of the maximum element found so far. If the current element is greater than this maximum, it is a leader.

Big-O Analysis:
- Time Complexity: O(n), where n is the number of elements in the array. We traverse the array once.
- Space Complexity: O(k), where k is the number of leaders found, as we store them in a list.
"""