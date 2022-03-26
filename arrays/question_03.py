# Container Trapping Rain Water
# Question: Given an array of integers representing an elevation map where the width of each bar is 1, return how many
# rainwater can be trapped.

# Examples:
# array = [] → 0
# array = [4] → 0
# array = [3, 4] → 0
# array = [1, 4, 2] → 0
# array = [1, 1, 0, 1] → 1
# array = [0, 0, 0, 0, 0] → 0
# array = [1, 0, 6, 3, 0, 7, 1, 0, 2, 1] → 13
# array = [1, 0, 8, 2, 0, 0, 7, 0, 9, 3, 0] → 27


def calculate_rain_waters(i, j, arr):
    return (j - i - 1) * min(arr[i], arr[j])


# O(n²) - Time Complexity
# O(1) - Space Complexity
def trapping_rain_water_01(array):
    length = len(array)
    if length <= 2 or array is None:
        return 0

    total_rw = 0

    for i in range(length):

        max_left = max_right = 0

        for j in range(i, -1, -1):
            max_left = max(max_left, array[j])

        for j in range(i, length):
            max_right = max(max_right, array[j])

        cur_rw = min(max_left, max_right) - array[i]

        if cur_rw > 0:
            total_rw += cur_rw

    return total_rw


# O(n) - Time Complexity
# O(1) - Space Complexity
def trapping_rain_water_02(array):
    length = len(array)
    if length <= 2 or array is None:
        return 0

    # total of rw, pointers and max value of each side
    rw, p_left, p_right, max_left, max_right = 0, 0, length - 1, 0, 0
    while p_left < p_right:
        left_value, right_value = array[p_left], array[p_right]

        # Case 01: move p_right (confirming that left side is a wall)
        if left_value > right_value:
            if right_value > max_right:
                max_right = right_value
            else:
                # no need to check left side, since we confirmed that is a wall
                rw += max_right - right_value
            p_right -= 1
        # Case 02: move p_left
        else:
            if left_value > max_left:
                max_left = left_value
            else:
                # no need to check right side, since we confirmed that is a wall
                rw += max_left - left_value
            p_left += 1
    return rw


# Went wrong in some cases
def trapping_rain_water_03(array):  # [5, 4, 1, 2]
    length = len(array)  # length = 4
    if length <= 2 or array is None:  # False or False
        return 0
    rw, i, j, prev_rw = 0, 0, 1, 0  # rw = 0, i = 0, j = 3, prev_rw = 5
    while j < length:  # True
        last_greatest = array[i]  # last_greatest = 5
        next_value = array[j]  # next_value = 2

        if next_value < last_greatest:  # True
            if (next_value > array[j - 1] and j == length - 2 and next_value >= array[j + 1]) or\
                    (next_value > array[j - 1] and j == length - 1):
                rw += calculate_rain_waters(i, j, array) - prev_rw
                prev_rw = 0
                i = j
            else:
                prev_rw += next_value
        elif next_value >= last_greatest:  #
            rw += calculate_rain_waters(i, j, array) - prev_rw
            prev_rw = 0
            i = j
        j += 1
    return rw


print(trapping_rain_water_01([10, 8, 1, 2]))
