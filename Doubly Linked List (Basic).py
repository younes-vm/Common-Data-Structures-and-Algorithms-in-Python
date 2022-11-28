# Check out singly linked lists in the repo as well
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self._head, self._tail, self._counter = None, None, 0

    def __len__(self):
        return self._counter

    def is_empty(self):
        return self._counter == 0

    def add_first(self, data):
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
        else:
            self._head.prev = Node(data)
            self._head.prev.next = self._head
            self._head = self._head.prev
        self._counter += 1

    def add_last(self, data):
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
        else:
            self._tail.next = Node(data)
            self._tail.next.prev = self._tail
            self._tail = self._tail.next
        self._counter += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception('Linked list is empty')
        data = self._head.data
        if self._counter == 1:
            self._head, self._tail = None, None
        else:
            self._head.next.prev = None
            self._head = self._head.next
        self._counter -= 1
        return data

    def remove_last(self):
        if self.is_empty():
            raise Exception('Linked list is empty')
        data = self._tail.data
        if self._counter == 1:
            self._head, self._tail = None, None
        else:
            self._tail.prev.next = None
            self._tail = self._tail.prev
        self._counter -= 1
        return data

    def first(self):
        if self.is_empty():
            raise Exception('Linked list is empty')
        return self._head.data

    def last(self):
        if self.is_empty():
            raise Exception('Linked list is empty')
        return self._tail.data
