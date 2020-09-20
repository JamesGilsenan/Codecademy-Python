from Singly_Linked_List import LinkedList
from Singly_Linked_List import Node

class MergedList(LinkedList):
    
    def merge_lists(self, head_1, head_2):
        if head_1 is None:
            return head_2
        if head_2 is None:
            return head_1

        dummy = temp = Node("") # initializing tail and temp as Node objects
        while head_1 is not None and head_2 is not None:
            if head_1.data < head_2.data:
                current = head_1
                head_1 = head_1.next
            else:
                current = head_2
                head_2 = head_2.next
            temp.next = current
            temp = temp.next
        temp.next = head_1 or head_2
        return dummy.next

 
merged_list = MergedList()        
my_list_A = LinkedList()
first_node_a = Node(1)
second_node_a = Node(3)
third_node_a = Node(5)
fourth_node_a = Node(7)
fifth_node_a = Node(9)
my_list_A.add_at_tail(first_node_a)
my_list_A.add_at_tail(second_node_a)
my_list_A.add_at_tail(third_node_a)
my_list_A.add_at_tail(fourth_node_a)
my_list_A.add_at_tail(fifth_node_a)

my_list_B = LinkedList()
first_node_b = Node(2)
second_node_b = Node(4)
third_node_b = Node(6)
fourth_node_b = Node(8)
fifth_node_b = Node(10)
my_list_B.add_at_tail(first_node_b)
my_list_B.add_at_tail(second_node_b)
my_list_B.add_at_tail(third_node_b)
my_list_B.add_at_tail(fourth_node_b)
my_list_B.add_at_tail(fifth_node_b)

print(my_list_A)
print(my_list_B)
head = merged_list.merge_lists(my_list_A.head, my_list_B.head)
