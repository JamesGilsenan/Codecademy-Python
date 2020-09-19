class Node:
    
    def __init__(self, data, position=0):
        self.data = data
        self.next = None
        self.position = position

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        current_node = self.head
        string = "["
        if self.head is None:
            return "Linked List is empty"
        while current_node is not None:
            string += str(current_node.data)
            if current_node.next is not None:
                string += ", "
            current_node = current_node.next
        string += "]"
        return string

    def get(self, index):
        if index > self.size() - 1:
            raise IndexError("List index is out of range")
        current = self.head
        count = 0
        found = False
        while current is not None and not found:
            if count == index:
                found = True
            else:
                current = current.next
                count += 1
        return current.data

    def add_at_head(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
    
    def add_at_tail(self, new_node):
        last_node = self.head
        while True:
            if last_node.next == None:
                break
            last_node = last_node.next
        last_node.next = new_node

    def add_at_index(self, index, new_node):
        temp = Node(new_node)
        current = self.head
        previous = None
        count = 0
        found = False
        if index > self.size():
            print("Cannot insert item. Index out of range")
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.next
                count += 1
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def delete_at_index(self, index):
        if index > self.size() - 1:
            raise IndexError("List index out of range")
        current = self.head
        previous = None
        count = 0
        found = False
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.next
                count += 1
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


    def size(self):
        count = 0
        last_node = self.head
        while True:
            if last_node.next == None:
                return count + 1
            last_node = last_node.next
            count += 1

        


first_node = Node("John")
second_node = Node("Ben")
third_node = Node("Paddy")
fourth_node = Node("Lad")
linked_list = LinkedList()

linked_list.add_at_head(first_node)
linked_list.add_at_head(second_node)
linked_list.add_at_tail(third_node)
#print(linked_list)
#linked_list.add_at_index(3, fourth_node)
#linked_list.delete_at_index(3)
print(linked_list.get(2))
print(linked_list)
print(linked_list.size())
