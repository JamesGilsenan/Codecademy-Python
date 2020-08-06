class SortedList(list):

    def append(self, value):
        super().append(value)
        self.sort()
        return self

mylist = SortedList([1,3,5])
print(mylist)
mylist.append(2)
print(mylist)
