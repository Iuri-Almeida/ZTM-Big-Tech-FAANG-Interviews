# Traversal a 2D Array using Breadth First Search

directions = [
        [-1, 0],  # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # lef
    ]


# O(n) - Time Complexity
# O(n) - Space Complexity
def __bfs_02(matrix):
    global directions

    seen = __create_bool_matrix(matrix)  # O(n) - TC, O(n) - SC
    values, queue = [], [(0, 0)]  # values: O(n) - SC

    while len(queue) > 0:  # O(n) - TC
        row, col = queue.pop(0)  # O(n) - TC [improve implementation]
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]:
            continue

        seen[row][col] = True
        values.append(matrix[row][col])  # O(1) -TC

        for i in range(len(directions)):  # O(4) - TC
            cur_direction = directions[i]
            queue.append((row + cur_direction[0], col + cur_direction[1]))
    return values


# O(1) - Time Complexity
# O(1) - Space Complexity
def __get_center_element(matrix):
    row = len(matrix) // 2
    col = len(matrix[0]) // 2
    return row, col


# O(n) - Time Complexity
# O(n) - Space Complexity
def __bfs(matrix):
    global directions

    seen = __create_bool_matrix(matrix)  # O(n) - TC, O(n) - SC

    row, col = __get_center_element(matrix)  # O(1) - TC, O(1) - SC
    seen[row][col] = True

    values, queue = [], [(row, col)]  # values: O(n) - SC

    min_height, max_height = 0, len(matrix) - 1
    min_width, max_width = 0, len(matrix[0]) - 1

    while len(queue) > 0:  # O(n) - TC
        row, col = queue.pop(0)  # O(n) - TC [improve implementation]
        values.append(matrix[row][col])  # O(1) -TC

        for i in range(len(directions)):  # O(4) - TC
            cur_direction = directions[i]
            new_row, new_col = row + cur_direction[0], col + cur_direction[1]
            if min_height <= new_row <= max_height and min_width <= new_col <= max_width and not seen[new_row][new_col]:
                seen[new_row][new_col] = True
                queue.append((new_row, new_col))
    return values


# O(n) - Time Complexity
# O(n) - Space Complexity
def __create_bool_matrix(mtx):
    matrix = []
    for _ in range(len(mtx)):
        matrix.append([False] * len(mtx[0]))
    return matrix


# O(n) - Time Complexity
# O(n) - Space Complexity
def traversal_2d_array_bfs(matrix):
    if not matrix or not matrix[0]:
        return matrix
    return __bfs(matrix)


m = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
print(traversal_2d_array_bfs(m))
