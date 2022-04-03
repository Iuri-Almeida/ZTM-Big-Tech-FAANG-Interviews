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
        return self.__heap[i] > self.__heap[j]

    def __max_child(self, idx):
        left, right = self.__left(idx), self.__right(idx)
        if left >= self.size() or right >= self.size():
            return None
        return left if self.__compare(left, right) else right

    def __sift_up(self):
        value_idx = self.size() - 1
        while value_idx > 0 and self.__compare(value_idx, self.__parent(value_idx)):
            self.__swap(self.__parent(value_idx), value_idx)
            value_idx = self.__parent(value_idx)

    def __sift_down(self):
        idx = 0
        max_child = self.__max_child(idx)
        while max_child is not None and self.__compare(max_child, idx):
            self.__swap(idx, max_child)
            idx = max_child
            max_child = self.__max_child(idx)

    def push(self, value):
        self.__heap.append(value)
        self.__sift_up()

    def pop(self):
        if self.is_empty():
            raise RuntimeError("The Priority Queue is empty!")
        self.__swap(0, self.size() - 1)
        greatest = self.__heap.pop()
        self.__sift_down()
        return greatest

    def peek(self):
        return self.__heap[0]

    def size(self):
        return len(self.__heap)

    def is_empty(self):
        return not self.__heap


pq = PriorityQueue()
pq.push(75)
pq.push(50)
pq.push(45)
pq.push(30)
pq.push(28)
pq.push(32)
pq.push(20)
print(pq)
print(pq.pop())
print(pq)
pq.push(64)
print(pq)
