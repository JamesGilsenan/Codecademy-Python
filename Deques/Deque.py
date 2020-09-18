#Deque is a double ended queue. A combonation of a stack and a queue. 
#Items can be added and removed from both end of a deque
class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item) 

    def remove_front(self):
        if self.items:
            self.items.pop()

    def remove_rear(self):
        if self.items:
            self.items.pop(0)

    def is_empty(self):
        if self.items == []:
            return True

    def size(self):
        if self.items:
            return len(self.items)
        return 0

    def __repr__(self):
        return "Object : {}".format(self.items)

    def peek_front(self):
        return self.items[-1]

    def peek_rear(self):
        return self.items[0]
