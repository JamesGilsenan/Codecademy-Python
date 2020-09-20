from Singly_Linked_List import LinkedList
from Singly_Linked_List import Node

class MyLinkedList(LinkedList):

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def traverse(self):
        current = self.head
        while current is not None:
            if current.next is not None:
                print(current.data, end="->")
            else:
                print(current.data)
            current = current.next

    def reverse_recursively(self, item):
        if item.next == None:
            self.head = item
            return
        self.reverse_recursively(item.next)
        temp = item.next
        temp.next = item
        item.next = None


my_list = MyLinkedList()
first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
my_list.add(first_node)
my_list.add(second_node)
my_list.add(third_node)
my_list.add(fourth_node)
my_list.add(fifth_node)

my_list.traverse()
my_list.reverse_recursively(my_list.head)
my_list.traverse()
