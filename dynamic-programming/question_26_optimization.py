# Min Cost Climbing Stairs
# Question: For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.
#
# Once you pay the cost for a step, you can either climb one or two steps. Find the minimum cost to reach the top of
# the staircase. Your first step can either be the first or second step.

# Ex.:
# cost = [20, 15, 30, 5] --> 20


def __min_cost_top_bottom(i, cost, cache):
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]
    if i in cache:
        return cache[i]
    cache[i] = cost[i] + min(__min_cost_top_bottom(i - 1, cost, cache), __min_cost_top_bottom(i - 2, cost, cache))
    return cache[i]


# O(n) - Time Complexity
# O(n) - Space Complexity
def min_cost_climbing_stairs(cost):
    length, cache = len(cost), dict()
    return min(__min_cost_top_bottom(length - 1, cost, cache), __min_cost_top_bottom(length - 2, cost, cache))


# O(n) - Time Complexity
# O(n) - Space Complexity
def __min_cost_bottom_up_01(cost):
    length, cache = len(cost), dict()
    for i in range(len(cost)):
        if i < 2:
            cache[i] = cost[i]
        else:
            cache[i] = cost[i] + min(cache[i - 1], cache[i - 2])
    return min(cache[length - 1], cache[length - 2])


# O(n) - Time Complexity
# O(1) - Space Complexity
def __min_cost_bottom_up_02(cost):
    length, first, second = len(cost), cost[0], cost[1]
    for i in range(2, len(cost)):
        first, second = second, cost[i] + min(first, second)
    return min(first, second)


print(__min_cost_bottom_up_02([20, 15, 30, 5]))
