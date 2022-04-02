# Validate Binary Search Tree
# Question: Given a Binary Tree, determine if it is a valid Binary Search Tree.

# Ex.:
# [] → True
# [1] → True
# [12, 7, 18, 5, 9, 16, 25] → True
# [6, 9, 10] → False
# [6, 4, 9, 2, 5, 1, 13] → False


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


# O(n) - Time Complexity
# O(n) - Space Complexity
def validate_bst_01(root: TreeNode):
    return __validate_01(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def __validate_01(node: TreeNode, min_val: TreeNode = None, max_val: TreeNode = None):
    if node is None:
        return True
    if max_val is not None and node.val >= max_val.val:
        return False
    if min_val is not None and node.val <= min_val.val:
        return False
    return __validate_01(node.left, min_val, node) and __validate_01(node.right, node, max_val)


# O(n) - Time Complexity
# O(n) - Space Complexity
def validate_bst_02(root: TreeNode):
    return __validate_02(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def __validate_02(node: TreeNode, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if node.val >= max_val or node.val <= min_val:
        return False
    return __validate_02(node.left, min_val, node.val) and __validate_02(node.right, node.val, max_val)


tree = TreeNode(15)
tree.left = TreeNode(12)
tree.left.left = TreeNode(10)
tree.left.right = TreeNode(16)
tree.right = TreeNode(17)
tree.right.left = TreeNode(16)
tree.right.right = TreeNode(18)
print(validate_bst_01(tree))
print(validate_bst_02(tree))
