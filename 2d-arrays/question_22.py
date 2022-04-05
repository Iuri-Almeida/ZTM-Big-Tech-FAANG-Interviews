# Walls and Gates
# Question: Given a 2D Array containing -1’s (walls), 0’s (gates) and INF’s (empty room). Fill each empty room with the
# number of steps to the nearest gate. If it is impossible to reach a gate, leave INF as the value. INF is equal to
# 2147483647.

# Ex.:
# [[INF, -1, 0, INF],
#  [INF, INF, INF, -1],
#  [INF, -1, INF, -1],
#  [0, -1, INF, INF]] →
# [[3, -1, 0, 1],
#  [2, 2, 1, -1],
#  [1, -1, 2, -1],
#  [0, -1, 3, 4]]

# [[INF, -1, 0, INF],
#  [-1, INF, INF, -1],
#  [INF, -1, INF, -1],
#  [0, -1, INF, INF]] →
#  [[INF, -1, 0, 1],
#  [-1, 2, 1, -1],
#  [1, -1, 2, -1],
#  [0, -1, 3, 4]]


def __get_gates(mtx):
    g = []
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == 0:
                g.append((i, j))
    return g


def __bfs(mtx):
    directions = [
        [-1, 0],  # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # left
    ]
    queue = __get_gates(mtx)
    queue_aux, count = len(queue), 1

    while len(queue) > 0:
        if queue_aux == 0:
            count += 1
            queue_aux = len(queue)

        row, col = queue.pop(0)
        queue_aux -= 1

        for i in range(len(directions)):
            cur_direction = directions[i]
            new_row, new_col = row + cur_direction[0], col + cur_direction[1]

            if new_row < 0 or new_col < 0 or new_row >= len(mtx) or new_col >= len(mtx[0]) or count > mtx[new_row][new_col]:
                continue

            mtx[new_row][new_col] = count
            queue.append((new_row, new_col))


def walls_and_gates_bfs(mtx):
    if not mtx or not mtx[0]:
        return mtx
    __bfs(mtx)
    return mtx


def __dfs(mtx, row, col, count=1):
    directions = [
        [-1, 0],  # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # left
    ]
    for i in range(len(directions)):
        cur_direction = directions[i]
        new_row, new_col = row + cur_direction[0], col + cur_direction[1]
        if new_row < 0 or new_col < 0 or new_row >= len(mtx) or new_col >= len(mtx[0]):
            continue
        if mtx[new_row][new_col] == float('inf') or count < mtx[new_row][new_col]:
            mtx[new_row][new_col] = count
            __dfs(mtx, new_row, new_col, count + 1)
    return


def __dfs_02(mtx, row, col, count=0):
    directions = [
        [-1, 0],  # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # left
    ]
    if row < 0 or col < 0 or row >= len(mtx) or col >= len(mtx[0]) or count > mtx[row][col]:
        return

    mtx[row][col] = count
    for i in range(len(directions)):
        cur_direction = directions[i]
        __dfs_02(mtx, row + cur_direction[0], col + cur_direction[1], count + 1)


def walls_and_gates_dfs(mtx):
    if not mtx or not mtx[0]:
        return mtx
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == 0:
                __dfs(mtx, i, j)
    return mtx


inf = float('inf')
m = [
    [inf, -1, 0, inf],
    [-1, inf, inf, -1],
    [inf, -1, inf, -1],
    [0, -1, inf, inf]
]
m2 = [
    [inf, -1, 0, inf],
    [-1, inf, inf, -1],
    [inf, -1, inf, -1],
    [0, -1, inf, inf]
]
result = walls_and_gates_bfs(m)
for r in result:
    print(r)
print()
result2 = walls_and_gates_dfs(m2)
for r in result2:
    print(r)
