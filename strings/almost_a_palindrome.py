# Almost a Palindrome
# Question: Given a string, determine if it is almost a palindrome. A string is almost a palindrome by removing 1
# letter. Consider only alphanumeric characters and ignore case sensitivity.

# Examples:
# s = “” → true
# s = null → false
# s = “raceacar” → true (racecar: true or racacar: true)
# s = “abccdba” → true (abcdba: false or abccba: true)
# s = “abcdefdba” → false (abcdefba: false or abdefdba: false)
# s = “aaaaaa” → true


# O(n) - Time Complexity
# O(1) - Space Complexity
def check_move(p1, p2, s):
    aux_p1, aux_p2 = p1, p2
    while aux_p1 < aux_p2:
        if s[aux_p1] != s[aux_p2]:
            return False
        aux_p1, aux_p2 = aux_p1 + 1, aux_p2 - 1
    return True


# O(n) - Time Complexity
# O(1) - Space Complexity
def almost_palindrome_01(s):
    if s is None:
        return False
    p1, p2 = 0, len(s) - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            p1_move = check_move(p1 + 1, p2, s)
            p2_move = check_move(p1, p2 - 1, s)
            return p1_move or p2_move
        p1, p2 = p1 + 1, p2 - 1
    return True


print(almost_palindrome_01(""))
