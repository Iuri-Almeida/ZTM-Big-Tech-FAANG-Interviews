# Average in Each Level of a Binary Tree
# Question: Given a Binary Tree, get the average value at each level of the tree.

# Ex.:
#     4
#    / \
#   7   9
#  / \   \
# 10  2   6
#      \
#       6
#      /
#     2
# Output: [4, 8, 6, 6, 2]


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


# O(n) - Time Complexity
# O(n) - Space Complexity
def average_in_each_level_01(root: TreeNode):
    if not root:
        return root

    data = {}
    _dfs_01(root, data)

    result = []
    for k in data:
        result.append(sum(data[k]) / len(data[k]))

    return result


# O(n) - Time Complexity
# O(n) - Space Complexity
def _dfs_01(node: TreeNode, data, depth=0):
    if not node:
        return node

    if depth not in data:
        data[depth] = []
    data[depth].append(node.val)

    _dfs_01(node.left, data, depth + 1)
    _dfs_01(node.right, data, depth + 1)


# O(n) - Time Complexity
# O(n) - Space Complexity
def average_in_each_level_02(root: TreeNode):
    if not root:
        return root

    data = {}
    _dfs_02(root, data)

    result = []
    for k in data:
        v, c = data[k]
        result.append(v / c)

    return result


# O(n) - Time Complexity
# O(n) - Space Complexity
def _dfs_02(node: TreeNode, data, depth=0):
    if not node:
        return node

    if depth not in data:
        data[depth] = (node.val, 1)
    else:
        v, c = data[depth]
        v += node.val
        c += 1
        data[depth] = (v, c)

    _dfs_02(node.left, data, depth + 1)
    _dfs_02(node.right, data, depth + 1)


# O(n) - Time Complexity
# O(n) - Space Complexity
def average_in_each_level_03(root: TreeNode):
    if not root:
        return root
    return _bfs_01(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def _bfs_01(root: TreeNode):
    result = []
    queue = [root]
    level_aux, level_arr, count = len(queue), [], 0
    while len(queue) > 0:
        cur_node = queue.pop(0)
        count += 1
        level_arr.append(cur_node.val)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)

        if count == level_aux:
            level_aux, count = len(queue), 0
            result.append(sum(level_arr) / len(level_arr))
            level_arr = []
    return result


# O(n) - Time Complexity
# O(n) - Space Complexity
def average_in_each_level_04(root: TreeNode):
    if not root:
        return root
    return _bfs_02(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def _bfs_02(root: TreeNode):
    result = []
    queue = [root]
    level_aux, level_tuple, count = len(queue), None, 0
    while len(queue) > 0:
        cur_node = queue.pop(0)
        count += 1
        if level_tuple is None:
            level_tuple = (cur_node.val, 1)
        else:
            v, c = level_tuple
            v += cur_node.val
            c += 1
            level_tuple = (v, c)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)

        if count == level_aux:
            level_aux, count = len(queue), 0
            v, c = level_tuple
            result.append(v / c)
            level_tuple = None
    return result


n = TreeNode(4)
n.left = TreeNode(7)
n.left.left = TreeNode(10)
n.left.right = TreeNode(2)
n.left.right.right = TreeNode(6)
n.left.right.right.left = TreeNode(2)
n.right = TreeNode(9)
n.right.right = TreeNode(6)
print(average_in_each_level_01(n))
print(average_in_each_level_02(n))
print(average_in_each_level_03(n))
print(average_in_each_level_04(n))
