# Number of Islands
# Question: Given a 2D array containing only 1’s (land) and 0’s (water), count the number of islands. An island is land
# connected horizontally or vertically.

# Ex.:
# [[1, 1, 1, 1, 0],
#  [1, 1, 0, 1, 0],
#  [1, 1, 0, 0, 1],
#  [0, 0, 0, 1, 1]] → 2

# [[0, 1, 0, 1, 0],
#  [1, 0, 1, 0, 1],
#  [0, 1, 1, 1, 0],
#  [1, 0, 1, 0, 1]] → 7


directions = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1]  # left
]


# O(n) - Time Complexity
# O(diagonal) - Space Complexity
def __bfs(mtx, seen, start_row, start_col):
    global directions

    queue = [(start_row, start_col)]

    while len(queue) > 0:
        row, col = queue.pop(0)
        if row < 0 or col < 0 or row >= len(mtx) or col >= len(mtx[0]) or seen[row][col] or mtx[row][col] == '0':
            continue

        seen[row][col] = True

        for i in range(len(directions)):
            cur_direction = directions[i]
            queue.append((row + cur_direction[0], col + cur_direction[1]))


# O(n) - Time Complexity
# O(n) - Space Complexity
def __create_bool_matrix(mtx):
    m_bool = []
    for _ in mtx:
        m_bool.append([False] * len(mtx[0]))
    return m_bool


# O(m * n) - Time Complexity
# O(max(m, n)) - Space Complexity
def number_of_islands(mtx):
    if not mtx or not mtx[0]:
        return 0

    seen = __create_bool_matrix(mtx)
    count = 0

    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == '1' and not seen[i][j]:
                __bfs(mtx, seen, i, j)
                count += 1
    return count


# O(n) - Time Complexity
# O(diagonal) - Space Complexity
def __bfs_02(mtx, start_row, start_col):
    global directions

    queue = [(start_row, start_col)]

    while len(queue) > 0:
        row, col = queue.pop(0)
        if row < 0 or col < 0 or row >= len(mtx) or col >= len(mtx[0]) or mtx[row][col] == '0':
            continue

        mtx[row][col] = '0'

        for i in range(len(directions)):
            cur_direction = directions[i]
            queue.append((row + cur_direction[0], col + cur_direction[1]))


# O(m * n) - Time Complexity
# O(max(m, n)) - Space Complexity
def number_of_islands_02(mtx):
    if not mtx or not mtx[0]:
        return 0

    count = 0

    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == '1':
                __bfs_02(mtx, i, j)
                count += 1
    return count


m = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["0", "1", "0", "0", "0"],
    ["1", "0", "1", "0", "1"]]
print(number_of_islands(m))
print(number_of_islands_02(m))
