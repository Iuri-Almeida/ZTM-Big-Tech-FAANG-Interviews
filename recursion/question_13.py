# Kth Largest Element in an Sorted Array
# Question: Given an unsorted array, return the kth largest element. It is the kth largest element in sorted order,
# not the kth distinct element.

# Ex.:
# nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 -> 4
from random import randint


# O(n) - Time Complexity
# O(n) - Space Complexity
def _merge(left, right):
    array = []
    left_len, right_len = len(left), len(right)
    p_left = p_right = 0

    while p_left < left_len and p_right < right_len:
        if left[p_left] < right[p_right]:
            array.append(left[p_left])
            p_left += 1
        else:
            array.append(right[p_right])
            p_right += 1
    return array + left[p_left:] + right[p_right:]


# Merge Sort
# O(n log n) - Time Complexity
# O(n) - Space Complexity
def merge_sort(arr):
    if not arr or len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    return _merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def quick_sort_01(arr):
    if len(arr) < 2:
        return arr

    left, pivot_array, right = [], [], []

    pivot = arr[randint(0, len(arr) - 1)]

    for value in arr:
        if value < pivot:
            left.append(value)
        elif value == pivot:
            pivot_array.append(value)
        elif value > pivot:
            right.append(value)

    return quick_sort_01(left) + pivot_array + quick_sort_01(right)


# O(1) - Time Complexity
# O(1) - Space Complexity
def __swap(arr, p1, p2):
    arr[p1], arr[p2] = arr[p2], arr[p1]


# O(n) - Time Complexity
# O(1) - Space Complexity
def __partition_index(arr, low, high):
    pivot = arr[high]
    p_idx = low

    for i in range(low, high):
        if arr[i] < pivot:
            __swap(arr, p_idx, i)
            p_idx += 1
    __swap(arr, p_idx, high)
    return p_idx


# O(n * log n) - Time Complexity
# O(log n) - Space Complexity
def __quick_sort_02(arr, l_idx, r_idx):
    if l_idx < r_idx:
        p_idx = __partition_index(arr, l_idx, r_idx)
        __quick_sort_02(arr, l_idx, p_idx - 1)
        __quick_sort_02(arr, p_idx + 1, r_idx)


# O(n²) - Time Complexity
# O(1) - Space Complexity (Tail Recursion)
def __quick_select(arr, l_idx, r_idx, idx_2_find):
    if l_idx <= r_idx:
        p_idx = __partition_index(arr, l_idx, r_idx)
        if p_idx == idx_2_find:
            return arr[p_idx]
        elif p_idx > idx_2_find:
            return __quick_select(arr, l_idx, p_idx - 1, idx_2_find)
        else:
            return __quick_select(arr, p_idx + 1, r_idx, idx_2_find)


def largest_element_with_merge_sort(nums, k):
    if k is None or nums is None or not nums:
        return nums
    return merge_sort(nums)[-k]


def largest_element_with_quick_sort_01(nums, k):
    if k is None or nums is None or not nums:
        return nums
    return quick_sort_01(nums)[-k]


def largest_element_with_quick_sort_02(nums, k):
    if k is None or nums is None or not nums:
        return nums
    __quick_sort_02(nums, 0, len(nums) - 1)
    return nums[-k]


def largest_element_with_quick_select(nums, k):
    if k is None or nums is None or not nums:
        return nums
    idx_2_find = len(nums) - k
    return __quick_select(nums, 0, len(nums) - 1, idx_2_find)
