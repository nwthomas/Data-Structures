class Queue:
    def __init__(self):
        """
        Initializes a new Queue and a size of 0
        """
        self.size = 0
        self.storage = []

    def enqueue(self, item):
        """
        Adds an item to the back of the Queue
        """
        self.size += 1
        self.storage = [item] + self.storage

    def dequeue(self):
        """
        Removes an item from the front of the queue
        and returns it
        """
        if self.size is 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(self.size)

    def len(self):
        """
        Returns the current length of the Queue
        """
        return self.size
