class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_linkedlist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def add_first(self, data):
        new_node = Node(data)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_last(self, data):
        new_node = Node(data)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, data):
        if(index == 0):
            self.add_first(data)
            return
        if(index >= self.length):
            self.add_last(data)
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

        self.length += 1

    def remove_first(self):
        if(self.length > 1):
            self.head = self.head.next
        if(self.length == 1):
            self.head = None
            self.tail = None
        if(self.length != 0):
            self.length -= 1

    def remove_last(self):
        if(self.length > 1):
            current = self.head
            for i in range(self.length - 2):
                current = current.next
            self.tail = current
            self.tail.next = None
        if(self.length == 1):
            self.head = None
            self.tail = None
        if(self.length != 0):
            self.length -= 1

    def remove(self, index):
        if(index == 0):
            self.remove_first()
            return
        if(index >= self.length):
            self.remove_last()
            return

        current = self.head
        for i in range(index - 1):
            current = current.next
        
        current.next = current.next.next
        self.length -= 1

    def remove_data(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                prev = current
            current = current.next

    def remove_dublicate(self):
        current = self.head
        seen = set()
        new_list = Linked_list()
        
        while current:
            if current.data not in seen:
                new_list.add_last(current.data)
                seen.add(current.data)
            current = current.next
        
        return new_list

    def __iter__(self):
        return LinkedIterator(self.head, self.length)

    def merge(linked_list1, linked_list2):
        merged_list = Linked_list()
        current1 = linked_list1.head
        current2 = linked_list2.head

        while current1 and current2:
            if current1.data < current2.data:
                merged_list.add_last(current1.data)
                current1 = current1.next
            else:
                merged_list.add_last(current2.data)
                current2 = current2.next

        while current1:
            merged_list.add_last(current1.data)
            current1 = current1.next

        while current2:
            merged_list.add_last(current2.data)
            current2 = current2.next

        return merged_list


class LinkedIterator():
    def __init__(self, head, length):
        self.head = head
        self.index = 0
        self.length = length

    def __iter__(self):
        return self
    
    def __next__(self): 
        if(self.index > self.length):
            raise StopIteration
        current = self.head
        for i in range(self.index):
            current = current.next
        self.index += 1
        return current.data

linked_list1 = Linked_list()
linked_list1.add_last(1)
linked_list1.add_last(3)
linked_list1.add_last(5)

linked_list2 = Linked_list()
linked_list2.add_last(1)
linked_list2.add_last(2)
linked_list2.add_last(4)

print()