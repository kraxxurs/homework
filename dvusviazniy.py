class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        current = self.head
        if current:
            for _ in range(self.length):
                print(current.data, end = " <-> ")
                current = current.next

    def add_first(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, data):
        if index <= 0:
            self.add_first(data)
            return
        if index >= self.length:
            self.add_last(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index):
            current = current.next

        new_node.previous = current.previous
        new_node.next = current
        current.previous.next = new_node
        current.previous = new_node
        self.length += 1

    def remove_first(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self.length -= 1

    def remove_last(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.length -= 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.remove_first()
            return
        if index == self.length - 1:
            self.remove_last()
            return

        current = self.head
        for _ in range(index):
            current = current.next

        current.previous.next = current.next
        current.next.previous = current.previous
        self.length -= 1


linked_list1 = DoubleLinkedList()
linked_list1.add_last(1)
linked_list1.add_last(3)
linked_list1.add_last(5)

linked_list1.print_list()