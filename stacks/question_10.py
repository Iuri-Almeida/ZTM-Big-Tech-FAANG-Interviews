# Valid Parentheses
# Question: Given a string containing only parentheses, determine if it is valid. The string is valid if all
# parentheses close.

# Ex.:
# s = “(())” → true
# s = “{{}}[]()” → true
# s = “([)]” → false
# s = “{[])” → false


# O(n) - Time Complexity
# O(n) - Space Complexity
def valid_parentheses(s):
    stack = []
    match = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in match:
            stack.append(char)
        else:
            if not stack or match[stack.pop()] != char:
                return False
    return not stack
