# To be honest, this is basically the basic version of the doubly linked list, renamed "deque"
# Doubly linked lists and deques (double ended queues) are pretty much equal in terms of basis and only differ when
# you want to add more features dependent on the ADT.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self._front, self._back, self._counter = None, None, 0

    def __len__(self):
        return self._counter

    def is_empty(self):
        return self._counter == 0

    def front_enqueue(self, data):
        if self.is_empty():
            self._front = Node(data)
            self._back = self._front
        else:
            self._front.prev = Node(data)
            self._front.prev.next = self._front
            self._front = self._front.prev
        self._counter += 1

    def back_enqueue(self, data):
        if self.is_empty():
            self._front = Node(data)
            self._back = self._front
        else:
            self._back.next = Node(data)
            self._back.next.prev = self._back
            self._back = self._back.next
        self._counter += 1

    def front_dequeue(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        data = self._front.data
        if self._counter == 1:
            self._front, self._back = None, None
        else:
            self._front.next.prev = None
            self._front = self._front.next
        self._counter -= 1
        return data

    def back_dequeue(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        data = self._back.data
        if self._counter == 1:
            self._front, self._back = None, None
        else:
            self._back.prev.next = None
            self._back = self._back.prev
        self._counter -= 1
        return data

    def front(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._front.data

    def back(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._back.data
