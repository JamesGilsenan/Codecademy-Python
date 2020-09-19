class Node:
    
    def __init__(self, data, position=0):
        self.data = data
        self.next = None
        self.position = position


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        if self.head is None:
            return "Linked List is empty"
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next
        return ""

    def get(self):
        pass

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

    def delete_at_index(self):
        pass

    def size(self):
        count = 0
        last_node = self.head
        while True:
            if last_node.next == None:
                return count + 1
            last_node = last_node.next
            count += 1

        


first_node = Node("John")
linked_list = LinkedList()
linked_list.add_at_head(first_node)
#print(linked_list)
second_node = Node("Ben")
linked_list.add_at_head(second_node)
#print(linked_list)
third_node = Node("Paddy")
linked_list.add_at_tail(third_node)
#print(linked_list)
fourth_node = Node("Lad")
#linked_list.add_at_head(fourth_node)
linked_list.add_at_index(10, fourth_node)
print(linked_list)
#print(linked_list.size())
#print(linked_list.index("Paddy"))