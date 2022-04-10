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


# O(1) - Time Complexity
# O(1) - Space Complexity
def __prob(k, s):
    return s / (8 ** k)


# O(k) - Time Complexity
# O(n) - Space Complexity
def __recursive(n, k, cur_row, cur_column, cache):
    if cur_row < 0 or cur_column < 0 or cur_row >= n or cur_column >= n:
        return 0
    if k == 0:
        return 1

    pos = str((cur_row, cur_column))
    if pos in cache:
        return cache[pos]

    global knight_movements

    cache[pos] = 0
    for mov in knight_movements:
        cache[pos] += __recursive(n, k - 1, cur_row + mov[0], cur_column + mov[1], cache)

    return cache[pos]


def knight_final_moves(n, k, row, column):
    cache = dict()
    return __prob(k, __recursive(n, k, row, column, cache))


n = 3
k = 2
row = 0
column = 0
print(knight_final_moves(n, k, row, column))
