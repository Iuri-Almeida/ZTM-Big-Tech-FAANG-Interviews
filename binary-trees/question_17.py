# Binary Tree Right Side View
# Question: Given a Binary Tree, imagine you’re standing to the right of the tree. Return an array of the values of the
# nodes you can see ordered from top to bottom.

# Ex.:
# [1, 2, 3, null, 5, null, 4] --> [1, 3, 4]
# [1, null, 3] --> [1, 3]
# [] --> []


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


# O(n) - Time Complexity
# O(n) - Space Complexity
def right_side_view_01(root: TreeNode):
    if not root:
        return root
    return _bfs(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def _bfs(root: TreeNode):
    if not root:
        return root
    result = []
    queue = [root]
    level_aux, level_last, count = len(queue), None, 0
    while len(queue) > 0:
        cur_node = queue.pop(0)
        count += 1
        level_last = cur_node.val
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)

        if count == level_aux:
            level_aux, count = len(queue), 0
            result.append(level_last)
    return result


# O(n) - Time Complexity
# O(n) - Space Complexity
def right_side_view_02(root: TreeNode):
    if not root:
        return root
    data = {}
    _dfs(root, data)
    return list(data.values())


# O(n) - Time Complexity
# O(n) - Space Complexity
def _dfs(node: TreeNode, data, depth=0):
    if not node:
        return node
    data[depth] = node.val
    _dfs(node.left, data, depth + 1)
    _dfs(node.right, data, depth + 1)


# O(n) - Time Complexity
# O(n) - Space Complexity
def right_side_view_03(root: TreeNode):
    if not root:
        return root
    data = []
    _dfs_02(root, data)
    return data


# O(n) - Time Complexity
# O(n) - Space Complexity
def _dfs_02(node: TreeNode, data, depth=1):
    if not node:
        return node
    if len(data) < depth:
        data.append(node.val)
    _dfs_02(node.right, data, depth + 1)
    _dfs_02(node.left, data, depth + 1)


node = TreeNode(3)
node.left = TreeNode(6)
node.left.left = TreeNode(9)
node.left.right = TreeNode(2)
node.left.left.right = TreeNode(5)
node.left.left.right.left = TreeNode(8)
node.right = TreeNode(1)
node.right.right = TreeNode(4)
print(right_side_view_01(node))
print(right_side_view_02(node))
print(right_side_view_03(node))
