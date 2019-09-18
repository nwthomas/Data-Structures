from math import floor


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        """
        Check if storage is empty, if it is start at beginning
        Put the value at the end of the list (append)
        If Arr[i] > Arr[i/2] then swap (parent is bigger)
        """
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    """
    Take in value
    """

    def delete(self):
        """
        """
        pass

    def get_max(self):
        """
        Return array position 0 on list (since it's a max-heap)
        """
        if len(self.storage) is 0:
            return None
        else:
            return self.storage[0]

    def get_size(self):
        """
        Return length property of array
        """
        return len(self.storage)

    def _bubble_up(self, i):
        """
        Helper function to compare to parent node and and switch if appropriate
        """
        p_index = floor((i - 1) / 2)
        while self.storage[i] > self.storage[p_index] and p_index >= 0:
            self.storage[i], self.storage[p_index] = (
                self.storage[p_index],
                self.storage[i],
            )
            i = p_index
            p_index = floor((p_index - 1) / 2)

    def _sift_down(self, index):
        """
        Helper function to compare to parent node and and switch if appropriate
        """
        pass
