# Rotting Oranges
# Question: Given a 2D Array containing 0’s (empty cell), 1’s (fresh orange) and 2’s (rotten orange). Every minute, all
# fresh oranges immediately adjacent (4 directions) to rotten oranges will rot. How many minutes must pass until all
# the oranges are rotten?

# Ex.:
# [[2, 1, 1],
#  [1, 1, 0],
#  [0, 1, 1]] → 4
# [[2, 1, 1],
#  [0, 1, 1],
#  [1, 0, 1]] → -1
# [[0, 2]] → 0
# [[2, 1, 0, 0, 0],
#  [1, 1, 0, 0, 0],
#  [0, 0, 0, 1, 2],
#  [0, 1, 0, 0, 1]] → -1


# O(m * n) - Time Complexity
# O(m * n) - Space Complexity
def __bfs(mtx):
    directions = [
        [-1, 0],  # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # left
    ]

    queue, fresh = __get_rotten_and_fresh(mtx)
    queue_aux, minutes = len(queue), 0

    while len(queue) > 0:
        if queue_aux == 0:
            minutes += 1
            queue_aux = len(queue)

        row, col = queue.pop(0)
        queue_aux -= 1

        for i in range(len(directions)):
            cur_direction = directions[i]
            new_row, new_col = row + cur_direction[0], col + cur_direction[1]
            if new_row < 0 or new_col < 0 or new_row >= len(mtx) or new_col >= len(mtx[0]) or mtx[new_row][new_col] != 1:
                continue
            mtx[new_row][new_col] = 2
            fresh -= 1
            queue.append((new_row, new_col))
    return -1 if fresh > 0 else minutes


# O(m * n) - Time Complexity
# O(m * n) - Space Complexity
def __get_rotten_and_fresh(mtx):
    r, f = [], 0
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == 1:
                f += 1
            elif mtx[i][j] == 2:
                r.append((i, j))
    return r, f


# O(m * n) - Time Complexity
# O(m * n) - Space Complexity
def rotting_oranges(mtx):
    if not mtx or not mtx[0]:
        return 0
    return __bfs(mtx)


m = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(rotting_oranges(m))
