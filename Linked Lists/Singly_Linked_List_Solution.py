#Time Complexity
# add -- O(1)
# size -- O(1) & O(n)
# append -- O(1) & O(n)
# search -- O(n)
# remove -- O(n)
# index -- O(n)
# insert -- O(n)
# pop -- O(n)  # can be O(1) if we use doubly linked list
# pop(k) -- O(k)

class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __repr__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        if self.tail is None:
            self.tail = temp
        self.length += 1

    def ssize(self):    #This is O(n)
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def size(self):     #This is O(1)
        return self.length

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:    #The item is the first item
            self.head = current.get_next()
        else:
            if current.get_next() is None:
                self.tail = previous    #In case the current tail is removed
            previous.set_next(current.get_next())
        self.length -= 1

    def __str__(self):
        current = self.head
        string = "["
        while current is not None:
            string += str(current.get_data())
            if current.get_next() is not None:
                string += ", "
            current = current.get_next()
        string += "]"
        return string

    def append(self, item):     #This is O(n) time complexity
        temp = Node(item)
        last = self.tail
        if last:
            last.set_next(temp)
        else:
            self.head = temp
        self.tail = temp
        self.length += 1

    def insert(self, index, item):
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        found = False
        if index > self.length - 1:
            raise IndexError("List index out of range")
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.get_next()
                count += 1
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        self.length += 1

    def index(self, item):
        position = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                position += 1
        if not found:
            raise ValueError("Value not present in the List")
        return position

    def pop(self, index=None):
        if index is None:
            index = self.length - 1
        if index > self.length - 1:
            raise IndexError("List index is out of range")
        current = self.head
        previous = None
        found = False
        if current:
            count = 0
            while current.get_next() is not None and not found:
                if count == index:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
                    count += 1
            if previous is None:
                self.head = current.get_next()
                if current.get_next() is None:
                    self.tail = current.get_next()
            else:
                self.tail = previous
                previous.set_next(current.get_next())
        self.length -= 1
        return current.get_data()    


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
linked_list = LinkedList()
#print(linked_list.is_empty())
linked_list.add(first_node)
linked_list.add(second_node)
linked_list.add(third_node)
print(linked_list)
#print(linked_list.is_empty())
#print(linked_list.ssize())
#linked_list.remove(third_node)
#linked_list.append(third_node)
#linked_list.insert(2, fourth_node)
#print(linked_list.index(first_node))
print(linked_list.pop(1))
print(linked_list)
print(linked_list.size())
