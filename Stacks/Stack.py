class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of our list.
        Returns nothing
        The runtime for this method is 0(1), or constant time, because appending
        to the end of the list happens in constant time.
        """

        self.items.append(item)
    
    def pop(self):
        """Returns and removes the last item for the list, which is also the top item 
        in the stack. 
        The runtime here is constant time, because all it does is index to the last item of the list.
        """
        if self.items:
            return self.items.pop()
        
        return None 

    def peek(self):
        """this method return the last item in the list, which is also
        the top item in the stack.
        This method runs in constant time because indexing into a list 
        is done in constant time"""
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """This method returns the length of the listthat is representing the stack.
        The method runs in constant time becasue finding the length of a list happens 
        in constant time
        """ 
        return len(self.items)

    def is_empty(self):
        """This method returns a boolean value describing whether or not the stack is empty.
        Testing for equality happensin constant time.
        """
        return self.items == []

my_stack = Stack()
my_stack.push("apple")
print(my_stack.items)
my_stack.push("banana")
my_stack.push("carrat")
print(my_stack.items)