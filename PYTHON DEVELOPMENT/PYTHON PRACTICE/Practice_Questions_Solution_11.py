# 11. **Binary Search**: Implement a binary search function that searches for a target value in a sorted list.


def binary_search(a, value):
    a.sort()

    def binary_search_recursive(a, value, low, high):
        if low > high:
            return -1

        middle_index = (low + high) // 2

        if a[middle_index] == value:
            return middle_index
        elif a[middle_index] > value:
            return binary_search_recursive(a, value, low, middle_index - 1)
        else:
            return binary_search_recursive(a, value, middle_index + 1, high)

    return binary_search_recursive(a, value, 0, len(a) - 1)

a = [1, 5, 6, 2, 9, 3, 4, 11, 7, 12, 13, 10, 8]
value = 6

index = binary_search(a, value)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
