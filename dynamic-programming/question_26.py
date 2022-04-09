# Min Cost Climbing Stairs
# Question: For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.
#
# Once you pay the cost for a step, you can either climb one or two steps. Find the minimum cost to reach the top of
# the staircase. Your first step can either be the first or second step.

# Ex.:
# cost = [20, 15, 30, 5] --> 20


def min_cost(i, cost):
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]
    return cost[i] + min(min_cost(i - 1, cost), min_cost(i - 2, cost))


# O(2^n) - Time Complexity
# O(n) - Space Complexity
def min_cost_climbing_stairs(cost):
    length = len(cost)
    return min(min_cost(length - 1, cost), min_cost(length - 2, cost))
