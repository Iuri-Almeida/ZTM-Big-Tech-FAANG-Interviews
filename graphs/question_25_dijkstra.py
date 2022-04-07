# Network Delay Time
# Question: There are n network nodes labeled 1 to N.
#
# Given a times array, containing edges represented by arrays [u, v, w] where u is the source node, v is the target
# node, and w is the time taken to travel from the source node to the target node.
#
# Send a signal from node k, return how long it takes for all nodes to receive the signal. Return -1 if it’s impossible.

# Ex.:
# n = 5, k = 1, times = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]] → 14
# n = 3, k = 2, times = [[2, 3, 4]] → -1
# n = 3, k = 1, times = [[1, 2, 8], [3, 1, 3]] → -1


class PriorityQueue(object):
    def __init__(self):
        self.__heap = []

    def __repr__(self):
        return str(self.__heap)

    @staticmethod
    def __parent(idx):
        return (idx - 1) // 2

    @staticmethod
    def __left(idx):
        return (idx * 2) + 1

    @staticmethod
    def __right(idx):
        return (idx * 2) + 2

    def __swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __compare(self, i, j):
        return self.__heap[i] < self.__heap[j]

    def __min_child(self, idx):
        left, right = self.__left(idx), self.__right(idx)
        if left >= self.size() or right >= self.size():
            return None
        return left if self.__compare(left, right) else right

    def __sift_up(self):
        value_idx = self.size() - 1
        while value_idx > 0 and self.__compare(value_idx, self.__parent(value_idx)):
            self.__swap(value_idx, self.__parent(value_idx))
            value_idx = self.__parent(value_idx)

    def __sift_down(self):
        value_idx = 0
        min_child = self.__min_child(value_idx)
        while min_child is not None and self.__compare(min_child, value_idx):
            self.__swap(value_idx, min_child)
            value_idx = min_child
            min_child = self.__min_child(value_idx)

    def push(self, value):
        self.__heap.append(value)
        self.__sift_up()

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Priory Queue is empty!")
        self.__swap(0, self.size() - 1)
        smaller = self.__heap.pop()
        self.__sift_down()
        return smaller

    def peek(self):
        return self.__heap[0]

    def size(self):
        return len(self.__heap)

    def is_empty(self):
        return not self.__heap


# O(n + e) - Time Complexity
# O(e) - Space Complexity
def _adjacent_list(n, times):
    adj_list = []
    for _ in range(n):
        adj_list.append([])
    for time in times:
        source, target, weight = time[0] - 1, time[1] - 1, time[2]
        adj_list[source].append((target, weight))
    return adj_list


# O(n) - Time Complexity
# O(n) - Space Complexity
def _create_dijkstra_list(n):
    dijkstra_list, inf = [], float('inf')
    for _ in range(n):
        dijkstra_list.append(inf)
    return dijkstra_list


# O(e * log n) - Time Complexity
# O(e + n) - Space Complexity
def network_delay_time(n, k, times):
    adj_list, dijkstra_list, heap = _adjacent_list(n, times), _create_dijkstra_list(n), PriorityQueue()
    dijkstra_list[k - 1] = 0
    heap.push(k - 1)
    while not heap.is_empty():
        cur_vertex = heap.pop()
        for node in adj_list[cur_vertex]:
            target, weight = node
            if dijkstra_list[cur_vertex] + weight < dijkstra_list[target]:
                dijkstra_list[target] = dijkstra_list[cur_vertex] + weight
                heap.push(target)
    max_value = max(dijkstra_list)
    return -1 if max_value == float('inf') else max_value


n = 3
k = 2
t = [[2, 3, 4]]
print(network_delay_time(n, k, t))
