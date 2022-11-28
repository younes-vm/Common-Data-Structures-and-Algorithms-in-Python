# This is an implementation of Queues using linked lists. There's an array implementation of queues in my repo.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._tail, self._head, self._counter = None, None, 0

    def is_empty(self):
        return self._counter == 0

    def __len__(self):
        return self._counter

    def enqueue(self, data):
        if self._head is None:
            self._head = Node(data)
            self._tail = self._head
        else:
            self._tail.next = Node(data)
            self._tail = self._tail.next
        self._counter += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        data = self._head.data
        self._head = self._head.next
        self._counter -= 1
        return data

    def front(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head.data
