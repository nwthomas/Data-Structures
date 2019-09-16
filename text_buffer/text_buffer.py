from doubly_linked_list import DoublyLinkedList

"""
We're using our own DLL because the runtime complexities for it are O(1)

Python's built-in lists are O(n) for the most part
"""


class TextBuffer:
  # If init is a string, we'll initialize the buffer with it
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        if init is not None:
            for char in init:
                self.contents.add_to_tail(char)

    def __str__(self):
        """
        Returns a string to print and replaces private string method in Python
        """
        text_buffer = ""
        current_node = self.contents.head
        while current_node:
            text_buffer += current_node.value
            current_node = current_node.next
        return text_buffer


tb = TextBuffer("Hello CS21")
print(tb)
