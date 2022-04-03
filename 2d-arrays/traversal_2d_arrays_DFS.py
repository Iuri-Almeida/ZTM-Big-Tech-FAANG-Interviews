# Traversal a 2D Array using Depth First Search

directions = [
        [-1, 0],  # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # lef
    ]


# O(n) - Time Complexity
# O(n) - Space Complexity
def __dfs(matrix, seen, values, row=0, col=0):
    global directions

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]:
        return

    seen[row][col] = True
    values.append(matrix[row][col])

    for i in range(len(directions)):
        cur_direction = directions[i]
        __dfs(matrix, seen, values, row + cur_direction[0], col + cur_direction[1])


# O(n) - Time Complexity
# O(n) - Space Complexity
def __create_bool_matrix(mtx):
    matrix = []
    for _ in range(len(mtx)):
        matrix.append([False] * len(mtx[0]))
    return matrix


# O(n) - Time Complexity
# O(n) - Space Complexity
def traversal_2d_array_dfs(matrix):
    if not matrix or not matrix[0]:
        return matrix

    seen = __create_bool_matrix(matrix)
    values = []

    __dfs(matrix, seen, values)
    return values


m = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
print(traversal_2d_array_dfs(m))
