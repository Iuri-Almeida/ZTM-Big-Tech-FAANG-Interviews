# Maximum Depth of Binary Tree
# Question: Given a binary tree, find its maximum depth. Maximum depth is the number of nodes along the longest path
# from the root node to the furthest leaf node.

# Ex.:
# null → 0
# [0, null, null] → 1
# [3, 9, 20, null, null, 15, 7] → 3


def max_depth(root):
    return _depth_01(root)


def _depth_01(root, depth=0, max_depth=0):
    if not root:
        return depth

    depth += 1
    max_depth = max(max_depth, depth)

    max_depth = max(max_depth, _depth_01(root.left, depth, max_depth))
    max_depth = max(max_depth, _depth_01(root.right, depth, max_depth))

    return max_depth


# O(n) - Time Complexity
# O(n) - Space Complexity
def _depth_02(root, depth=0):
    if not root:
        return depth
    depth += 1
    return max(_depth_02(root.left, depth), _depth_02(root.right, depth))
