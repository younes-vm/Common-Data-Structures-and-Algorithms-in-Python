"""
This is an array based queue. I have also uploaded an implementation using linked lists. Check out the repo.
Note that this code is for queues with maximum capacities, I've implemented another code without this limitation.
Check out "Queue - Array (Unlimited) (Basic).py" in the repo.
"""


class Queue:
    DEFAULT_CAPACITY = 100

    def __init__(self, queue_size=None):
        if queue_size is None:
            queue_size = Queue.DEFAULT_CAPACITY
        self._max = queue_size
        self._data = [None] * self._max
        self._counter = 0
        self._front = 0

    def __len__(self):
        return self._counter

    def is_empty(self):
        return self._counter == 0

    def front(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]

    def enqueue(self, data):
        if self._counter == self._max:
            raise Exception('Queue is full')
        self._data[(self._front + self._counter) % self._max] = data
        self._counter += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        data = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._max
        self._counter -= 1
        return data
