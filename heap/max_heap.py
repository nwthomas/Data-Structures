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
        # print(self.storage)
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
            self.storage[i], self.storage[p_index] = (
                self.storage[p_index],
                self.storage[i],
            )
            i = p_index
            p_index = floor((p_index - 1) / 2)

    def _sift_down(self, i):
        """
        Helper function to compare to parent node and and switch if appropriate
        """
        # print(self.storage)
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
            if right_compare < left_compare and right_compare < 0:
                self.storage[i], self.storage[right] = (
                    self.storage[right],
                    self.storage[i],
                )
                self._sift_down(right)
            elif left_compare <= right_compare and left_compare < 0:
                self.storage[i], self.storage[left] = (
                    self.storage[left],
                    self.storage[i],
                )
                self._sift_down(left)
        elif left:
            if self.storage[i] < self.storage[left]:
                self.storage[i], self.storage[left] = (
                    self.storage[left],
                    self.storage[i],
                )
                self._sift_down(left)
        elif right:
            if self.storage[i] < self.storage[right]:
                self.storage[i], self.storage[right] = (
                    self.storage[right],
                    self.storage[i],
                )
                self._sift_down(right)


# l = Heap()
# l.insert(10)
# l.insert(5)
# l.insert(9)
# l.insert(4)
# l.insert(7)
# l.insert(2)
# l.insert(3)
# l.insert(12)
# print(l.delete())
