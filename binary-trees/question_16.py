# Binary Tree Level Order Traversal
# Question: Given a Binary Tree, return the level order traversal of the nodes’ values as an array.

# Ex.:
# [] → []
# null → []
# [1] → [[1]]
# [3,9,20,null,null,15,7] → [[3], [9, 20], [15, 7]]


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# O(n) - Time Complexity
# O(n) - Space Complexity
def level_order_01(root: TreeNode):
    if not root:
        return root

    data = dict()
    _dfs(root, data)

    arr = []
    for k in data:
        arr.append(data[k])

    return arr


# O(n) - Time Complexity
# O(n) - Space Complexity
def _dfs(node: TreeNode, data, depth=1):
    if not node:
        return node

    if depth not in data:
        data[depth] = []
    data[depth].append(node.val)

    _dfs(node.left, data, depth + 1)
    _dfs(node.right, data, depth + 1)


# O(n) - Time Complexity
# O(n) - Space Complexity
def level_order_02(root: TreeNode):
    if not root:
        return root
    return _bfs(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def _bfs(root: TreeNode):
    result = []
    queue = [root]
    level_aux, level_arr, counter = len(queue), [], 0
    while len(queue) > 0:
        cur_node = queue.pop(0)
        counter += 1
        level_arr.append(cur_node.val)

        if cur_node.left is not None:
            queue.append(cur_node.left)

        if cur_node.right is not None:
            queue.append(cur_node.right)

        if counter == level_aux:
            level_aux, counter = len(queue), 0
            result.append(level_arr)
            level_arr = []
    return result


node = TreeNode(3)
node.left = TreeNode(6)
node.left.left = TreeNode(9)
node.left.right = TreeNode(2)
node.left.left.right = TreeNode(5)
node.left.left.right.left = TreeNode(8)
node.right = TreeNode(1)
node.right.right = TreeNode(4)
print(level_order_01(node))
print(level_order_02(node))
