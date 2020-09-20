from Singly_Linked_List import LinkedList
from Singly_Linked_List import Node

def reverse_list(linked_list):
    current = linked_list.head
    previous = None

    while current.next:
        temp = current.next 
        current.next = previous  
        previous = current       
        current = temp      
    current.next = previous
    linked_list.head = current




my_list = LinkedList()
first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
my_list.add_at_head(first_node)
my_list.add_at_tail(second_node)
my_list.add_at_tail(third_node)
my_list.add_at_tail(fourth_node)
my_list.add_at_tail(fifth_node)

print(my_list)
reverse_list(my_list)
print(my_list)