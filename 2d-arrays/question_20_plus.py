# Max Area if Island
# Question: You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area
# of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in grid. If
# there is no island, return 0.

# Ex.:
# [[1, 1, 1, 1, 0],
#  [1, 1, 0, 1, 0],
#  [1, 1, 0, 0, 1],
#  [0, 0, 0, 1, 1]] → 9

# [[0, 1, 0, 1, 0],
#  [1, 0, 1, 0, 1],
#  [0, 1, 1, 1, 0],
#  [1, 0, 1, 0, 1]] → 5


directions = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1]  # left
]


def __bfs(mtx, seen, start_row, start_col):
    global directions

    queue = [(start_row, start_col)]
    area = 0

    while len(queue) > 0:
        row, col = queue.pop(0)
        if row < 0 or col < 0 or row >= len(mtx) or col >= len(mtx[0]) or seen[row][col] or mtx[row][col] == 0:
            continue

        seen[row][col] = True
        area += 1

        for i in range(len(directions)):
            cur_direction = directions[i]
            queue.append((row + cur_direction[0], col + cur_direction[1]))
    return area


def __create_bool_matrix(mtx):
    m_bool = []
    for _ in mtx:
        m_bool.append([False] * len(mtx[0]))
    return m_bool


def max_of_islands(mtx):
    if not mtx or not mtx[0]:
        return 0

    seen = __create_bool_matrix(mtx)
    max_area = 0

    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == 1 and not seen[i][j]:
                max_area = max(max_area, __bfs(mtx, seen, i, j))
    return max_area


def __bfs_02(mtx, start_row, start_col):
    global directions

    queue = [(start_row, start_col)]
    area = 0

    while len(queue) > 0:
        row, col = queue.pop(0)
        if row < 0 or col < 0 or row >= len(mtx) or col >= len(mtx[0]) or mtx[row][col] == 0:
            continue

        mtx[row][col] = 0
        area += 1

        for i in range(len(directions)):
            cur_direction = directions[i]
            queue.append((row + cur_direction[0], col + cur_direction[1]))
    return area


def max_of_islands_02(mtx):
    if not mtx or not mtx[0]:
        return 0

    max_area = 0

    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == 1:
                max_area = max(max_area, __bfs_02(mtx, i, j))
    return max_area


m = [[0, 0, 0, 0, 0, 0, 0, 0]]
print(max_of_islands(m))
print(max_of_islands_02(m))
