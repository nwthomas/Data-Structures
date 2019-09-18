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

    def delete(self):
        """
        Removes the highest value (first array position) and
        sorts the rest of the heap progressively
        """
        top = self.storage[0]
        if self.get_size() > 1:
            self.storage[0] = self.storage.pop()
        else:
            self.storage.pop()
        self._sift_down(0)
        return top

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
            self._swap(i, p_index)
            i = p_index
            p_index = floor((p_index - 1) / 2)

    def _sift_down(self, i):
        """
        Helper function to compare to parent node and and switch if appropriate
        """
        # Find left/right indices
        left = (2 * i) + 1
        right = (2 * i) + 2

        # Find if left/right exist
        if left > self.get_size() - 1:
            left = None
        if right > self.get_size() - 1:
            right = None

        # Control flow for comparing/switching values
        if left and right:
            left_compare = self.storage[i] - self.storage[left]
            right_compare = self.storage[i] - self.storage[right]
            if left_compare <= right_compare and left_compare < 0:
                self._swap(i, left)
                self._sift_down(left)
            elif right_compare < left_compare and right_compare < 0:
                self._swap(i, right)
                self._sift_down(right)
        elif left:
            if self.storage[i] < self.storage[left]:
                self._swap(i, left)
                self._sift_down(left)
        elif right:
            if self.storage[i] < self.storage[right]:
                self._swap(i, right)
                self._sift_down(right)

    def _swap(self, i1, i2):
        self.storage[i1], self.storage[i2] = self.storage[i2], self.storage[i1]
