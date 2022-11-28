# This is the linked list implementation of a stack, there is also ab array implementation. You will find it in the repo
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class LinkedListStack:
    def __init__(self):
        self._head = None
        self._tail = None
        self._counter = 0

    def __len__(self):
        return self._counter

    def is_empty(self):
        if self._counter == 0:
            return True
        else:
            return False

    def push(self, data):
        if self.is_empty():
            self._head = Node(data)
            self._tail = self._head
        else:
            new_tail = Node(data)
            new_tail.prev = self._tail
            self._tail = new_tail
        self._counter += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            data = self._tail.data
            self._tail = self._tail.prev
            self._counter -= 1
            return data

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._tail.data
