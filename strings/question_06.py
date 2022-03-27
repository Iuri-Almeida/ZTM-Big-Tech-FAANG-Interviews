# Valid Palindrome
# Question: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring
# case sensitivity.

# Examples:
# s = “” → true
# s = null → false
# s = “AbcCBa” → true
# s = “a! a, a a: aa” → true
# s = “ab, cd” → false
# s = “aaaaaa” → true
# s = “hello, world!” → false


# O(n) - Time Complexity
# O(n) - Space Complexity
def valid_palindrome_01(s):  # "AbcCBa"
    if s is None:
        return False
    reversed_string = updated_string = ""  # reversed_string = "abccba", updated_string = "abccba"
    length = len(s)  # length = 6
    for i in range(length):  # i = 6
        left_char, right_char = s[i], s[length - 1 - i]  # left_char = a, right_char = A
        if left_char.isalnum():  # True
            updated_string += left_char.lower()
        if right_char.isalnum():  # True
            reversed_string += right_char.lower()
    return updated_string == reversed_string


# O(n) - Time Complexity
# O(n) - Space Complexity
def valid_palindrome_02(s):
    if s is None:
        return False
    updated_string = ""
    for i in range(len(s)):
        if s[i].isalnum():
            updated_string += s[i].lower()

    p1, p2 = 0, len(updated_string) - 1
    while p1 < p2:
        if updated_string[p1] != updated_string[p2]:
            return False
        p1, p2 = p1 + 1, p2 - 1
    return True


# O(n) - Time Complexity
# O(n) - Space Complexity
def valid_palindrome_03(s):
    if s is None:
        return False
    updated_string = ""
    for i in range(len(s)):
        if s[i].isalnum():
            updated_string += s[i].lower()

    length = len(updated_string)
    p1 = length // 2 - 1
    p2 = p1 + 1
    if length % 2 != 0:
        p1 += 1
    while p1 >= 0 and p2 < length:
        if updated_string[p1] != updated_string[p2]:
            return False
        p1, p2 = p1 - 1, p2 + 1
    return True


# O(n) - Time Complexity
# O(1) - Space Complexity
def valid_palindrome_04(s):
    if s is None:
        return False

    p1, p2 = 0, len(s) - 1
    while p1 < p2:
        if not s[p1].isalnum() or not s[p2].isalnum():
            while not s[p1].isalnum():
                p1 += 1
                if p1 >= p2:
                    break
            while not s[p2].isalnum():
                p2 -= 1
                if p2 <= p1:
                    break
        else:
            if s[p1].lower() != s[p2].lower():
                return False
            p1, p2 = p1 + 1, p2 - 1
    return True
