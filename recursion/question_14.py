# Find First and Last Position of Element in Sorted Array
# Question: Given an array of integers sorted in ascending order, return the starting and ending index of a given
# target value in an array, i.e. [x, y]. Your solution should run in O(log n) time.

# Ex.:
# nums = [5, 7, 7, 8, 8, 10], target = 8 -> [3, 4]
# nums = [5, 7, 7, 8, 8, 10], target = 6 -> [-1, -1]
# nums = [], target = 0 -> [-1, -1]
# nums = [1], target = 1 -> [0, 0]
# nums = [1, 1], target = 1 -> [0, 1]
# nums = [0, 0, 0, 1, 2, 3], target = 0 -> [0, 2]


# O(n) - Time Complexity
# O(1) - Space Complexity
def find_first_and_last_01(nums, target):
    if not nums or target is None:
        return [-1, -1]

    p1, p2 = 0, len(nums) - 1
    while p1 <= p2:
        mid = (p1 + p2) // 2
        if target == nums[mid]:
            first_pos = mid - 1
            while first_pos >= 0 and target == nums[first_pos]:
                first_pos -= 1
            last_pos = mid + 1
            while last_pos < len(nums) and target == nums[last_pos]:
                last_pos += 1
            return [first_pos + 1, last_pos - 1]
        elif target > nums[mid]:
            p1 = mid + 1
        else:
            p2 = mid - 1
    return [-1, -1]


# O(log n) - Time Complexity
# O(1) - Space Complexity
def __binary_search(nums, p1, p2, target):
    while p1 <= p2:
        mid = (p1 + p2) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            p1 = mid + 1
        else:
            p2 = mid - 1
    return -1


# O(log n) - Time Complexity
# O(1) - Space Complexity
def find_first_and_last_02(nums, target):
    # check inputs
    if not nums or target is None:
        return [-1, -1]

    # check if target exists in nums
    first_pos = __binary_search(nums, 0, len(nums) - 1, target)
    if first_pos == -1:
        return [-1, -1]

    # define the start and end position
    start_pos = end_pos = first_pos
    start_temp = start_pos
    end_temp = end_pos

    # left binary search
    while start_pos != -1:
        start_temp = start_pos
        start_pos = __binary_search(nums, 0, start_pos - 1, target)
    start_pos = start_temp

    # right binary search
    while end_pos != -1:
        end_temp = end_pos
        end_pos = __binary_search(nums, end_pos + 1, len(nums) - 1, target)
    end_pos = end_temp

    return [start_pos, end_pos]
