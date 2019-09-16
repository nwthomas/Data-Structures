"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """
        Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to.
        """
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """
        Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to.
        """
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """
        Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode.
        """
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly.
        """
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node  # Important to set pointer for old head node
            self.head = new_node

    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        second node the new head node of the List.
        Returns the value of the removed Node
        """
        node_value = self.head.value
        self.delete(self.head)
        return node_value

    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly.
        """
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node  # Important to set pointer for old tail node
            self.tail = new_node

    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        node_value = self.tail.value
        self.delete(self.tail)
        return node_value

    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        """
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

        self.add_to_head(value)

    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    def delete(self, node):
        """
        Removes a node from the list and handles cases where
        the node was the head or the tail
        """
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = self.head.next
            node.delete()
        elif self.tail is node:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        """
        Returns the highest value currently in the list
        """
        if self.length is 0:
            return None
        else:
            highest = self.head.value
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
                if highest < current_node.value:
                    highest = current_node.value
            return highest
