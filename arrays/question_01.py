# Two Sum - Google Interview
# Question: Given an array of integers, return the indices of the two numbers that add up to a given target.

# Examples:
# nums = [], target = 1 → None, null
# nums = [3], target = 3 → None, null
# nums = None, null, target = None → None, null
# nums = [0, 1, 7, 2, 4, 5], target = 0 → None, null
# nums = [2, 1, 4, 6, 9], target = 6 → [0, 2]
# nums = [1, 2], target = 3 → [0, 1]


# O(n²) - Time Complexity
# O(1) - Space Complexity
def two_sum_01(nums, target):
    length = len(nums)
    if length <= 1 or nums is None or target is None:
        return None
    for i in range(length):
        num_to_find = target - nums[i]
        for j in range(i + 1, length):
            if nums[j] == num_to_find:
                return [i, j]
    return None


# O(n) - Time Complexity
# O(n) - Space Complexity
def two_sum_02(nums, target):
    length = len(nums)  # 3
    if length <= 1 or nums is None or target is None:  # False or False or False
        return None
    complements = dict()  # {1: 0, 0: 1, -3: 2}
    for i in range(length):  # i =
        cur_num = nums[i]  # cur_num =
        if cur_num in complements:  #
            return [complements[cur_num], i]  #
        complement = target - cur_num  # complement =
        complements[complement] = i
    return None  # None


# [1, 3, 2, 5, 6], 5
print(two_sum_02([1, 2, 5], 2))
