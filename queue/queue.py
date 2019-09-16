from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        """
        Initializes a new Queue and a size of 0
        """
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        """
        Adds an item to the back of the Queue
        """
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        """
        Removes an item from the front of the queue
        and returns it
        """
        if self.size > 0:
            self.size -= 1
            head_item = self.storage.head
            self.storage.remove_from_head()
            return head_item.value
        else:
            return None

    def len(self):
        """
        Returns the current length of the Queue
        """
        return self.size
