# Check out doubly linked lists in the repo as well
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            new_head = Node(data)
            new_head.next = self._head
            self._head = new_head
        self._counter += 1

    def add_last(self, data):
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
        else:
            self._tail.next = Node(data)
            self._tail = self._tail.next
        self._counter += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception('Linked list is empty')
        data = self._head.data
        if self._counter == 1:
            self._head, self._tail = None, None
        else:
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
            t = self._head
            i = 1
            while i < self._counter - 1:
                t = t.next
                i += 1
            t.next = None
            self._tail = t
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
