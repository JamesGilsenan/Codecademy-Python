class SortedList(list):

    def __init__(self, list):
        super().__init__(list)
        self.sort()

    def append(self, value):
        super().append(value)
        self.sort()
        return self

mylist = SortedList([1,5,3,9])
print(mylist)
mylist.append(2)
print(mylist)
