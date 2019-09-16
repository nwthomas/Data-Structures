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

    def append(self, value):
        """
        Adds a new character to the back of the text buffer
        """
        for i in range(len(value)):
            self.contents.add_to_tail(value[i])
        return self.__str__()

    def prepend(self, value):
        """
        Adds a new character to the front of the text buffer
        """
        for i in range(len(value) - 1, -1, -1):
            self.contents.add_to_head(value[i])
        return self.__str__()

    def delete_back(self, num_delete):
        """
        Removes a character from the back of the text buffer
        """
        for i in range(num_delete):
            self.contents.remove_from_tail()
        return self.__str__()

    def delete_front(self, num_delete):
        """
        Remvoes a character from the front of the text buffer
        """
        for i in range(num_delete):
            self.contents.remove_from_head()
        return self.__str__()

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
tb.append(" Dude.")
tb.delete_front(6)
tb.prepend("This is nuts. ")
tb.delete_back(1)
print(tb)
