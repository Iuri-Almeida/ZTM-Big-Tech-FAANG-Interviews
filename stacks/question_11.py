# Minimum Remove to Make Valid Parentheses
# Question: Given a string only containing round brackets ‘(‘ and ‘)’ and lowercase characters, remove the least amount
# of brackets so the string is valid. A string is considered valid if it is empty or if there are brackets, they all
# close.

# Ex.:
# s = “” → “”
# s = “(“ → “”
# s = “)(“ → “”
# s = “()()” → “()()”
# s = “(helloword)” → “(helloword)”
# s = “(hello)world” → “(hello)world”
# s = “(hello()w)orld(” → “(hello()w)orld”
# s = "(word)(((something)here))" →


# O(n) - Time Complexity
# O(n) - Space Complexity
def minimum_remove_to_make_valid_parentheses_01(s: str):
    stack = []
    s = list(s)
    for i in range(len(s)):
        # Case 01: "("
        if s[i] == "(":
            stack.append(s[i])
        # Case 02: ")"
        elif s[i] == ")":
            if stack:
                stack.pop()
            else:
                s[i] = ""
    # check stack
    if stack:
        i, j = 0, -1
        while i < len(stack):
            if s[j] == "(":
                s[j] = ""
                i += 1
            j -= 1
    return "".join(s)


# O(n) - Time Complexity
# O(n) - Space Complexity
def minimum_remove_to_make_valid_parentheses_02(s: str):
    stack = []
    s = list(s)
    for i in range(len(s)):
        # Case 01: "("
        if s[i] == "(":
            stack.append(i)
        # Case 02: ")"
        elif s[i] == ")":
            if stack:
                stack.pop()
            else:
                s[i] = ""
    # check stack
    while len(stack) > 0:
        s[stack.pop()] = ""
    return "".join(s)


print(minimum_remove_to_make_valid_parentheses_01("())))"))
