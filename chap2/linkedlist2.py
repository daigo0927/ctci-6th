class Node(object):
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)
        
class LinkedList(object):
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        if value is not None:
            self.append(value)

    def __len__(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(str(node))
            node = node.next
        return '->'.join(values)

    def append(self, value):
        # append node to the tail of linkedlist, and return the tail node
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def append_all(self, values):
        for v in values:
            self.append(v)
        return self.tail

    def pad_head(self):
        head_new = Node(0, next_node=self.head)
        self.head = head_new


class DoublyLinkedList(LinkedList):
    def append(self, value):
        if self.head is None:
            self.tail = self.head = Node(value, next_node=None, prev_node=self.tail)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return
