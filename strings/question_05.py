# Longest Substring Without Repeating Characters
# Question: Given a string, find the length of the longest substring without repeating characters.

# Examples:
# s = “” → 0
# s = “aaaaaa” → 1
# s = “abcd” → 4
# s = “aabbcd” → 3
# s = “abcdeffdabcehti” → 9
# s = "abcbda" → 4


# O(n²) - Time Complexity
# O(n) - Space Complexity
def longest_substring_without_repeating_characters_01(s):  # s = "abcbda"
    length = len(s)
    # start max substring at 0
    max_substring = 0
    # start first loop
    for p1 in range(length):
        first_char = s[p1]
        # define set
        chars = set()
        # add p1 to set
        chars.add(first_char)
        # start second loop
        for p2 in range(p1 + 1, length):
            second_char = s[p2]
            # check if p2 already in set
            if second_char in chars:
                # if so, break
                break
            # if not, add to set
            chars.add(second_char)
        # compare max substring with set length
        max_substring = max(max_substring, len(chars))
        # check if p2 reached the last char
        if length - p1 == len(chars):
            break
    return max_substring


# Time Limit Exceeded
def longest_substring_without_repeating_characters_02(s):
    window = len(s)
    while window > 1:
        p1, p2 = 0, window
        while p2 <= len(s):
            chars = set()
            for i in range(p1, p2):
                if s[i] in chars:
                    p1 += 1
                    p2 += 1
                    break
                chars.add(s[i])
            # check if it is the largest substring
            if len(chars) == window:
                return window
        window -= 1
    return window


# O(n) - Time Complexity
# O(n) - Space Complexity
def longest_substring_without_repeating_characters_03(s):
    length = len(s)
    p1 = p2 = max_window = 0
    chars = set()
    while p2 < length:
        char = s[p2]
        if char in chars:
            p1 += 1
            p2 = p1
            max_window = max(max_window, len(chars))
            chars = set()
        else:
            chars.add(char)
            p2 += 1
    return max(max_window, len(chars))


# O(n) - Time Complexity
# O(n) - Space Complexity
def longest_substring_without_repeating_characters_04(s):  # "abcbda"
    length = len(s)
    p1 = max_window = 0
    chars = dict()
    for p2 in range(length):
        char = s[p2]
        if char in chars and chars[char] >= p1:
            p1 = chars[char] + 1
        chars[char] = p2
        max_window = max(max_window, p2 - p1 + 1)
    return max_window


print(longest_substring_without_repeating_characters_04("aabbcd"))
