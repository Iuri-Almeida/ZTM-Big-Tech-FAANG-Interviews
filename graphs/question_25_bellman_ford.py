# Network Delay Time
# Question: There are n network nodes labeled 1 to N.
#
# Given a times array, containing edges represented by arrays [u, v, w] where u is the source node, v is the target
# node, and w is the time taken to travel from the source node to the target node.
#
# Send a signal from node k, return how long it takes for all nodes to receive the signal. Return -1 if it’s impossible.

# Ex.:
# n = 5, k = 1, times = [[1, 2, 9], [1, 4, 2], [2, 5, -3], [4, 2, -4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]] → 14
# n = 3, k = 2, times = [[2, 3, 4]] → -1
# n = 3, k = 1, times = [[1, 2, 8], [3, 1, 3]] → -1


# O(n) - Time Complexity
# O(n) - Space Complexity
def __create_distances(n):
    d, inf = [], float('inf')
    for _ in range(n):
        d.append(inf)
    return d


# O(n * e) - Time Complexity
# O(n) - Space Complexity
def network_delay_time(n, k, times):
    distances = __create_distances(n)
    distances[k - 1] = 0
    for _ in range(n - 1):
        count = 0
        for time in times:
            source, target, weight = time[0] - 1, time[1] - 1, time[2]
            if distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight
                count += 1
        if count == 0:
            break
    max_value = max(distances)
    return -1 if max_value == float('inf') else max_value


n = 5
k = 1
times = [[1, 2, 9], [1, 4, 2], [2, 5, -3], [4, 2, -4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(network_delay_time(n, k, times))
