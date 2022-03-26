# Backspace String Compare
# Question: Given two strings S and T, return true if they are equal when both are typed out. Any ‘#’ that appears in
# the string counts as a backspace.

# Examples:
# s = “”, t = “aaa” → False
# s = “”, t = “aaa###” → True
# s = “aa”, t = “###aaa” → False
# s = “#aa#”, t = “a#a#a” → True


# O(n) - Time Complexity
# O(n) - Space Complexity
def backspace_string_compare_01(s, t):  # s = "ab#c", t = "acz#"
    array_s, array_t = [], []  # array_s = ["a", "c"], array_t = ["a", "c"]
    for char in s:  # char = "c"
        if array_s and char == "#":
            array_s.pop()
        elif char != "#":  #
            array_s.append(char)

    for char in t:
        if array_t and char == "#":
            array_t.pop()
        elif char != "#":
            array_t.append(char)

    return array_s == array_t


# O(m) - Time Complexity
# O(n) - Space Complexity
def update_array(array, string):
    for char in string:
        if array and char == "#":
            array.pop()
        elif char != "#":
            array.append(char)


# O(n + m) - Time Complexity
# O(n + m) - Space Complexity
def backspace_string_compare_02(s, t):  # s = "ab#c", t = "acz#"
    array_s, array_t = [], []  # array_s = ["a", "c"], array_t = ["a", "c"]
    update_array(array_s, s)
    update_array(array_t, t)

    return array_s == array_t


# O(n + m) - Time Complexity
# O(1) - Space Complexity
def backspace_string_compare_03(s, t):
    p1, p2 = len(s) - 1, len(t) - 1

    while p1 >= 0 or p2 >= 0:
        if s[p1] == "#" or t[p2] == "#":
            if s[p1] == "#":
                back_count = 2
                while back_count > 0:
                    p1 -= 1
                    back_count -= 1
                    if s[p1] == "#":
                        back_count += 2
            if t[p2] == "#":
                back_count = 2
                while back_count > 0:
                    p2 -= 1
                    back_count -= 1
                    if t[p2] == "#":
                        back_count += 2
        else:
            if s[p1] != t[p2]:
                return False
            else:
                p1 -= 1
                p2 -= 1
    return True
