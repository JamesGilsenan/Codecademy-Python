class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """This method takes in an item and inserts that item into the 0th  index of the list
        that is representing the Queue
        
        The runtime is 0(n), or linear time, because inserting into the 0th index of a list
        forces all the other items in the list to move one index to the right
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Return and removes the front most item of the Queue which is represented by the last item
        in the list.
        
        The runtime is 0(1), or constant time, because indexing to the end of a list happens in
        constant time
        """
        if self.items:
            self.items.pop()
        return None

    def peek(self):
        """Returns the last item in the list which represents the front most item in the queue.

        The runtime is constant time becasue we're just indexing to the last item of the list
        and return the value found there. 
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Return the size of the Queue which is represented by t he length of the list.
        
        The runtime is 0(1), constant time, because we're only return the length
        """
        return len(self.items)

    def is_empty(self):
        """Returns a boolean value expressing whether or not the list represnting the queue is empty

        The runtime is constant time as a test for equality occurs in constant time
        """
        return self.items == [] 

my_q = Queue()