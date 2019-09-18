class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        """
        Check if stroage is empty, if it is start at beginning
        Put the value at the end of the list (append)
        If Arr[i] > Arr[i/2] then swap (parent is bigger)
        """
        pass

    def delete(self):
        """
        """
        pass

    def get_max(self):
        """
        Return array position 0 on list (since it's a max-heap)
        """
        pass

    def get_size(self):
        """
        Return length property of array
        """
        return len(self.storage)

    def _bubble_up(self, index):
        """
        Helper function to compare to parent node and and switch if appropriate
        """
        pass

    def _sift_down(self, index):
        """
        Helper function to compare to parent node and and switch if appropriate
        """
        pass
