# Knight Probability in Chessboard
# Question: On a given n x n chessboard, a knight piece will start at the r-th row and c-th column. The knight will
# attempt to make k moves.
#
# A knight can move in 8 possible ways. Each move will choose one of these 8 at random. The knight continues moving
# until it finishes k moves, or it moves off the chessboard. Return the probability that the knight is on the chessboard
# after it finishes moving.

# Ex.:
# n = 3, k = 2, row = 0, column = 0 --> 0.06250
# n = 1, k = 0, row = 0, column = 0 --> 1.00000
# n = 6, k = 2, row = 2, column = 2 --> 0.53125
# n = 6, k = 1, row = 2, column = 2 --> 1.00000


knight_movements = [
    [-2, 1],  # up-right
    [-2, -1],  # up-left
    [-1, 2],  # right-up
    [1, 2],  # right-down
    [2, 1],  # down-right
    [2, -1],  # down-left
    [-1, -2],  # left-up
    [1, -2]  # left-down
]


def __prob(k, s):
    return s / (8 ** k)


def __create_mtx(n):
    mtx = []
    for _ in range(n):
        r = []
        for _ in range(n):
            r.append(0)
        mtx.append(r)
    return mtx


def __recursive(mtx, k, cur_row, cur_column, count=0):
    if cur_row < 0 or cur_column < 0 or cur_row >= len(mtx) or cur_column >= len(mtx[0]):
        return 0
    if count == k:
        return 1

    global knight_movements

    total = 0
    for mov in knight_movements:
        total += __recursive(mtx, k, cur_row + mov[0], cur_column + mov[1], count + 1)

    return total


def knight_final_moves(n, k, row, column):
    mtx = __create_mtx(n)
    return __prob(k, __recursive(mtx, k, row, column))


n = 2
k = 0
row = 1
column = 1
print(knight_final_moves(n, k, row, column))
