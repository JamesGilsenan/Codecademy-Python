class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        string = "["
        current = self.head
        while current is not None:
            if current.next is None:
                string += str(current.data)
            else:
                string += str(current.data) + ", "
            current = current.next
        string += "]"
        return string

    def add_at_head(self, item):
        current = self.head
        if current is None:
            self.head = item
        else:
            item.next = current
            current.previous = item
            self.head = item
        self.length += 1

    def add_at_tail(self, item):
        current = self.head
        if current is None:
            self.head = item
            self.length += 1        
            return
        while current.next is not None:
            current = current.next
        item.previous = current
        current.next = item
        self.length += 1        

    def add_at_index(self, index, item): #Adds item before index passed in
        current = self.head
        print(current)
        count = 0
        found = False
        while current is not None and not found:
            if count == index:
                found = True
            else:
                current = current.next
            count += 1
        if index == 0:
            self.add_at_head(item)
        elif index == self.length:
            self.add_at_tail(item)
        elif index >= self.length:
            raise IndexError("List index out of range")
        else:
            previous = current.previous
            item.previous = previous
            item.next = current
            previous.next = item
            current.previous = item
        self.length += 1
        
    def get(self, index):
        current = self.head
        count = 0
        found = False
        while current is not None and not found:
            if count == index:
                found = True
            else:
                current = current.next
            count += 1
        if index >= self.length:
            raise IndexError("List index out of range")
        else:
            return current.data

    def delete_at_index(self, index):
        current = self.head
        count = 0
        found = None
        while current is not None and not found:
            if count == index:
                found = True
            else:
                current = current.next
            count += 1
        if index >= self.length:
            raise IndexError("List index out of range")
        elif index == 0:
            temp = current.next
            current.next = None
            temp.previous = None
            self.head = temp
        elif index == self.length - 1:
            previous = current.previous
            previous.next = None
            current.previous = None
        else:
            temp = current.next
            previous = current.previous
            previous.next = temp
            temp.previous = previous
        self.length - 1

"""
first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
d_linked_list = DoublyLinkedList()

d_linked_list.add_at_head(first_node)
d_linked_list.add_at_head(second_node)
d_linked_list.add_at_tail(third_node)
print(d_linked_list)
#d_linked_list.add_at_index(4, fourth_node)
#print(d_linked_list.get(3))
d_linked_list.delete_at_index(3)
print(d_linked_list)
"""