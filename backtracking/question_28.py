# Sudoku Solver
# Question: Create a function that solves for any 9x9 sudoku puzzle given.

# Ex.:
# Input: board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: [
#   ["5","3","4","6","7","8","9","1","2"],
#   ["6","7","2","1","9","5","3","4","8"],
#   ["1","9","8","3","4","2","5","6","7"],
#   ["8","5","9","7","6","1","4","2","3"],
#   ["4","2","6","8","5","3","7","9","1"],
#   ["7","1","3","9","2","4","8","5","6"],
#   ["9","6","1","5","3","7","2","8","4"],
#   ["2","8","7","4","1","9","6","3","5"],
#   ["3","4","5","2","8","6","1","7","9"]
# ]


# O(1) - Time Complexity
# O(1) - Space Complexity
def __get_box_id(row, col):
    row_val = (row // 3) * 3
    col_val = col // 3
    return row_val + col_val


# O(n) - Time Complexity
# O(n) - Space Complexity
def __get_set(n):
    arr = []
    for _ in range(n):
        arr.append(set())
    return arr


# O(n²) - Time Complexity
# O(1) - Space Complexity
def __fill_not_empty_cells(board, boxes, rows, cols):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != ".":
                val, box_id = board[r][c], __get_box_id(r, c)
                boxes[box_id].add(val)
                rows[r].add(val)
                cols[c].add(val)


# O(1) - Time Complexity
# O(1) - Space Complexity
def __is_valid(box, row, col, val):
    return val not in box and val not in row and val not in col


# O((n!)^n) - Time Complexity
# O(n²) - Space Complexity
def __solve_backtrack(board, boxes, rows, cols, cur_row=0, cur_col=0):
    if cur_row == len(board) or cur_col == len(board[0]):
        return True

    if board[cur_row][cur_col] == ".":
        for num in range(1, len(board) + 1):
            num_val = str(num)

            # adding to board
            board[cur_row][cur_col] = num_val

            box_id = __get_box_id(cur_row, cur_col)
            box, row, col = boxes[box_id], rows[cur_row], cols[cur_col]

            # checking if num_val already exists
            if __is_valid(box, row, col, num_val):
                box.add(num_val)
                row.add(num_val)
                col.add(num_val)

                if cur_col == len(board[0]) - 1:
                    if __solve_backtrack(board, boxes, rows, cols, cur_row + 1, 0):
                        return True
                else:
                    if __solve_backtrack(board, boxes, rows, cols, cur_row, cur_col + 1):
                        return True

                # deleting num_val
                box.remove(num_val)
                row.remove(num_val)
                col.remove(num_val)

            board[cur_row][cur_col] = "."

    else:
        if cur_col == len(board[0]) - 1:
            if __solve_backtrack(board, boxes, rows, cols, cur_row + 1, 0):
                return True
        else:
            if __solve_backtrack(board, boxes, rows, cols, cur_row, cur_col + 1):
                return True


def sudoku_solver(board):
    board_len = len(board)

    # creating our data structures
    boxes, rows, cols = __get_set(board_len), __get_set(board_len), __get_set(board_len)

    # filling with numbers that are already on the board
    __fill_not_empty_cells(board, boxes, rows, cols)

    __solve_backtrack(board, boxes, rows, cols)

    return board


b = [
  ["5", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
r = sudoku_solver(b)
for i in r:
    print(i)
