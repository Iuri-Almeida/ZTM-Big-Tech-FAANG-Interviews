# Implement a Binary Search


def __mid(i, j):
    return (i + j) // 2


# O(log n) - Time Complexity
# O(1) - Space Complexity
def binary_search(arr, target):
    if not arr or not target:
        return None
    p1, p2 = 0, len(arr) - 1
    while p1 <= p2:
        mid = __mid(p1, p2)
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            p1 = mid + 1
        else:
            p2 = mid - 1
    return None
