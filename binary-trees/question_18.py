# Count Complete Tree Nodes
# Question: Given a complete Binary Tree, count the number of nodes.

# Ex.:
# [1, 2, 3, 4, 5, 6] --> 6
# [] --> 0
# [1] --> 1


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


# O(n) - Time Complexity
# O(n) - Space Complexity
def count_tree_nodes_01(root: TreeNode):
    if not root:
        return 0
    return _bfs(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def _bfs(root: TreeNode):
    if not root:
        return 0
    queue, level_nodes = [root],  0
    while len(queue) > 0:
        cur_node = queue.pop(0)
        level_nodes += 1
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)
    return level_nodes


# O(n) - Time Complexity
# O(n) - Space Complexity
def count_tree_nodes_02(root: TreeNode):
    if not root:
        return 0
    return _dfs(root)


# O(n) - Time Complexity
# O(n) - Space Complexity
def _dfs(root: TreeNode, total=0):
    if not root:
        return total
    total += 1
    total = _dfs_01(root.left, total)
    total = _dfs_01(root.right, total)
    return total


# O(h²) - Time Complexity
# O(1) - Space Complexity
def count_tree_nodes_04(root: TreeNode):
    if not root:
        return 0

    height = __get_tree_height(root)
    if height == 0:
        return 1

    upper_count = (2 ** height) - 1

    left, right = 0, upper_count
    while left < right:
        idx_to_find = __mid(left, right)
        if __node_exists(idx_to_find, height, root):
            left = idx_to_find
        else:
            right = idx_to_find - 1
    return upper_count + left + 1


# O(1) - Time Complexity
# O(1) - Space Complexity
def __mid(i, j):
    n = i + j
    return n // 2 + (1 if n % 2 else 0)


# O(h) - Time Complexity
# O(1) - Space Complexity
def __get_tree_height(root: TreeNode):
    cur_node, height = root, 0
    while cur_node.left is not None:
        height += 1
        cur_node = cur_node.left
    return height


# O(h) - Time Complexity
# O(1) - Space Complexity
def __node_exists(idx_to_find, height, node: TreeNode):
    left, right, count = 0, (2 ** height) - 1, 0
    while count < height:
        mid_of_node = __mid(left, right)
        if idx_to_find >= mid_of_node:
            node = node.right
            left = mid_of_node
        else:
            node = node.left
            right = mid_of_node - 1
        count += 1
    return node is not None


n = TreeNode(1)
n.left = TreeNode(2)
n.left.left = TreeNode(3)
n.left.right = TreeNode(4)
n.right = TreeNode(9)
n.right.left = TreeNode(7)
n.right.right = TreeNode(5)
print(count_tree_nodes_01(n))
print(count_tree_nodes_02(n))
print(count_tree_nodes_04(n))
