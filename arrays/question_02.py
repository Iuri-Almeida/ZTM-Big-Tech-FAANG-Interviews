# Container With Most Water
# Question: You are given an array of positive integers where each integer represents the height of a vertical line on
# a chart. Find two lines which together with the x-axis forms a container that would hold the greatest amount of water.
# Returns the area of water it would hold.

# Examples:
# array = [] → 0
# array = [4] → 0
# array = [3, 4] → 3 * 1 = 3
# array = [1, 1, 0, 1] → 1 * 3 = 3
# array = [0, 0, 0, 0, 0] → 0 * 0 = 0
# array = [1, 8, 2, 7, 9, 3] → 8 * 3 = 24


# O(n²) - Time Complexity
# O(1) - Space Complexity
def container_with_most_water_01(array):  # array = [0, 0, 0, 0, 0]
    length = len(array)  #
    # check wrong inputs
    if length <= 1 or array is None:  #
        return 0  #
    # define a max area (all positive integers)
    max_area = 0  # max_area =
    for i in range(length):  # i =
        for j in range(i + 1, length):  # j =
            # min between the two values
            height = min(array[i], array[j])  # height =
            # distance between the two values
            width = j - i  # width =
            # get area
            area = height * width  # area =
            # check max area
            max_area = max(max_area, area)
    return max_area  # 3


# O(n) - Time Complexity
# O(1) - Space Complexity
def container_with_most_water_02(array):  # [1, 8, 2, 7, 9, 3]
    length = len(array)  # length = 6
    if length <= 1 or array is None:  # False or False
        return 0

    # define a max area (all positive integers)
    max_area = 0  # max_area = 24

    # define pointers (start, end)
    left, right = 0, length - 1  # left = 4, right = 4

    while left < right:  # False
        left_value = array[left]  # left_value =
        right_value = array[right]  # right_value =

        width = right - left  # width =
        height = min(left_value, right_value)  # height =
        area = width * height  # area =

        max_area = max(max_area, area)

        if left_value < right_value:  #
            left += 1
        else:
            right -= 1

    return max_area


print(container_with_most_water_02([1, 1]))
