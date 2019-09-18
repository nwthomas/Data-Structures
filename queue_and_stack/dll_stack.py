import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        node_value = self.storage.head.value
        self.storage.remove_from_head()
        self.size -= 1
        return node_value

    def len(self):
        return self.size
