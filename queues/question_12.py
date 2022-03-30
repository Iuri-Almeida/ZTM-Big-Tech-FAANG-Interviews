# Implement Queue using Stacks
# Question: Implement the class Queue using Stacks. The queue methods you need to implement are enqueue, dequeue, peek
# and is_empty.

# O(n) - Space Complexity
class Stack(object):
    def __init__(self):
        self.array = []

    def __repr__(self):
        return str(self.array)

    # O(1) - Time Complexity
    def push(self, value):
        self.array.append(value)

    # O(1) - Time Complexity
    def pop(self):
        return self.array.pop()

    # O(1) - Time Complexity
    def peek(self):
        return self.array[-1]

    # O(1) - Time Complexity
    def size(self):
        return len(self.array)

    # O(1) - Time Complexity
    def is_empty(self):
        return not self.array


class Queue01(object):
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return str(self.stack)

    def __reverse_stack(self):
        l, r = 0, len(self.stack) - 1
        while l < r:
            self.stack[l], self.stack[r] = self.stack[r], self.stack[l]
            l, r = l + 1, r - 1

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.__reverse_stack()
        removed = self.stack.pop()
        self.__reverse_stack()
        return removed

    def peek(self):
        self.__reverse_stack()
        first = self.stack[-1]
        self.__reverse_stack()
        return first

    def is_empty(self):
        return len(self.stack) == 0


# O(n) - Space Complexity
class Queue02(object):
    def __init__(self):
        self.stack_01 = Stack()
        self.stack_02 = Stack()

    def __repr__(self):
        return str([self.stack_01, self.stack_02])

    # O(n) - Time Complexity
    def __stack_01_to_stack_02(self):
        for _ in range(self.stack_01.size()):
            self.stack_02.push(self.stack_01.pop())

    # O(1) - Time Complexity
    def push(self, value):
        self.stack_01.push(value)

    # O(n) - Time Complexity
    def pop(self):
        if self.stack_02.is_empty():
            self.__stack_01_to_stack_02()
        return self.stack_02.pop()

    # O(n) - Time Complexity
    def peek(self):
        if self.stack_02.is_empty():
            self.__stack_01_to_stack_02()
        return self.stack_02.peek()

    # O(1) - Time Complexity
    def empty(self):
        return self.stack_01.is_empty() and self.stack_02.is_empty()


myQueue_02 = Queue02()
myQueue_02.push(1)  # // queue is: [1]
print(myQueue_02)
myQueue_02.push(2)  # // queue is: [1, 2] (leftmost is front of the queue)
print(myQueue_02)
print(myQueue_02.peek())  # // return 1
print(myQueue_02.pop())  # // return 1, queue is [2]
print(myQueue_02)
print(myQueue_02.empty())  # // return false
